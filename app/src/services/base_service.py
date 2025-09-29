from typing import List

from app.src.constants import DEFAULT_PAGE, DEFAULT_SIZE
from app.src.dtos.base_dto import BaseDto
from app.src.entities.base_entity import BaseEntity
from app.src.repositories.base_repository import BaseRepository


class BaseService:
    def __init__(self, repository: BaseRepository):
        self._repository = repository

    async def create(self, dto: BaseDto) -> BaseEntity:
        return await self._repository.create(dto)

    async def get_by_id(self, id: int) -> BaseEntity:
        return await self._repository.get_by_id(id)

    async def get_by_attribute(
        self, attribute_name: str, attribute_value
    ) -> BaseEntity:
        return await self._repository.get_by_attribute(attribute_name, attribute_value)

    async def get_list(
        self, page: int = DEFAULT_PAGE, size: int = DEFAULT_SIZE
    ) -> tuple[List[BaseEntity], int]:
        return await self._repository.get_list(page, size)

    async def update(self, id: int, dto: BaseDto) -> BaseEntity:
        return await self._repository.update(id, dto)

    async def delete(self, id: int) -> bool:
        return await self._repository.delete(id)
