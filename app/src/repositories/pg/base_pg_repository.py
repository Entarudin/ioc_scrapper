from typing import List, Any, AsyncIterator

from sqlalchemy import select, func

from app.src.constants.pagination import DEFAULT_BATCH_SIZE
from app.src.dtos.base_dto import BaseDto
from app.src.entities.base_entity import BaseEntity
from app.src.exceptions.exception import (
    ServiceError,
    EntityDoesNotExistError,
    InvalidOperationError,
)
from app.src.models import BaseModel
from abc import ABC, abstractmethod
from app.src.adapters.sqlalchemy import Adapter as SQLAlchemyAdapter
from app.src.repositories.base_repository import BaseRepository
from app.src.constants import DEFAULT_PAGE, DEFAULT_SIZE


class BasePgRepository(BaseRepository, ABC):
    def __init__(self, adapter: SQLAlchemyAdapter):
        self.__adapter = adapter

    @abstractmethod
    def _get_entity_type(self) -> type[BaseEntity]:
        pass

    @abstractmethod
    def _get_model_type(self) -> type[BaseModel]:
        pass

    def _map_dto_to_model(self, dto: BaseDto) -> BaseModel:
        return self._get_model_type()(**dto.model_dump())

    def _map_model_to_entity(self, model: BaseModel) -> BaseEntity:
        return self._get_entity_type().model_validate(model)

    def _map_models_to_entities(self, models: List[BaseModel]) -> List[BaseEntity]:
        return [self._map_model_to_entity(m) for m in models]

    async def create(self, dto: BaseDto) -> BaseEntity:
        try:
            async with self.__adapter.get_session() as session:
                model = self._map_dto_to_model(dto)
                session.add(model)
                await session.commit()
                await session.refresh(model)
                return self._map_model_to_entity(model)
        except Exception as e:
            raise ServiceError(message=str(e), name="DatabaseError") from e

    async def get_by_id(self, id: int) -> BaseEntity:
        async with self.__adapter.get_session() as session:
            stmt = select(self._get_model_type()).where(self._get_model_type().id == id)
            result = await session.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise EntityDoesNotExistError(
                    message=f"{self._get_model_type().__name__} with id={id} not found"
                )
            return self._map_model_to_entity(model)

    async def get_by_attribute(
        self, attribute_name: str, attribute_value
    ) -> BaseEntity:
        async with self.__adapter.get_session() as session:
            model_cls = self._get_model_type()
            stmt = select(model_cls).where(
                getattr(model_cls, attribute_name) == attribute_value
            )
            result = await session.execute(stmt)
            model = result.scalar_one_or_none()
            if not model:
                raise EntityDoesNotExistError(
                    message=f"{model_cls.__name__} with {attribute_name}={attribute_value} not found"
                )
            return self._map_model_to_entity(model)

    async def get_list(
        self, page: int = DEFAULT_PAGE, size: int = DEFAULT_SIZE
    ) -> tuple[List[BaseEntity], int]:
        async with self.__adapter.get_session() as session:
            stmt = select(self._get_model_type()).offset((page - 1) * size).limit(size)
            result = await session.execute(stmt)
            models = result.scalars().all()
            items = self._map_models_to_entities(models)
            count = await self.count()
            return items, count

    async def get_batch_by_conditions(
        self,
        *conditions: Any,
        batch_size: int = DEFAULT_BATCH_SIZE,
        order_field: None = None,
        order_by: None = None,
        **filters,
    ) -> AsyncIterator[List[BaseEntity]]:
        async with self.__adapter.get_session() as session:
            if order_field is None:
                order_field = self._get_model_type().id
            last_value = None

            while True:
                stmt = (
                    select(self._get_model_type())
                    .filter(*conditions)
                    .filter_by(**filters)
                    .limit(batch_size)
                )

                if last_value is not None:
                    stmt = stmt.filter(order_field > last_value)

                stmt = stmt.order_by(order_field.asc())

                if order_by:
                    stmt = stmt.order_by(order_field.asc(), *order_by)

                result = await session.execute(stmt)
                batch = result.scalars().all()

                if not batch:
                    break

                yield self._map_models_to_entities(batch)
                last_value = getattr(batch[-1], order_field.key)

    async def update(self, id: int, dto: BaseDto) -> BaseEntity:
        async with self.__adapter.get_session() as session:
            model_cls = self._get_model_type()
            model = await session.get(model_cls, id)
            if not model:
                raise EntityDoesNotExistError(
                    message=f"{model_cls.__name__} with id={id} not found"
                )

            for key, value in dto.model_dump().items():
                setattr(model, key, value)

            await session.commit()
            await session.refresh(model)
            return self._map_model_to_entity(model)

    async def delete(self, id: int) -> bool:
        async with self.__adapter.get_session() as session:
            model_cls = self._get_model_type()
            model = await session.get(model_cls, id)
            if not model:
                raise InvalidOperationError(
                    message=f"{model_cls.__name__} with id={id} does not exist and cannot be deleted"
                )

            await session.delete(model)
            await session.commit()
            return True

    async def count(self) -> int:
        async with self.__adapter.get_session() as session:
            stmt = select(func.count()).select_from(self._get_model_type())
            result = await session.execute(stmt)
            return result.scalar_one()
