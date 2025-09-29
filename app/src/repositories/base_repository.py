from abc import ABC, abstractmethod
from typing import List
from app.src.constants import DEFAULT_PAGE, DEFAULT_SIZE

from app.src.dtos.base_dto import BaseDto
from app.src.entities.base_entity import BaseEntity


class BaseRepository(ABC):
    @abstractmethod
    async def create(self, dto: BaseDto) -> BaseEntity:
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> BaseEntity:
        pass

    @abstractmethod
    async def get_by_attribute(
        self, attribute_name: str, attribute_value
    ) -> BaseEntity:
        pass

    @abstractmethod
    async def get_list(
        self, page: int = DEFAULT_PAGE, size: int = DEFAULT_SIZE
    ) -> tuple[List[BaseEntity], int]:
        pass

    @abstractmethod
    async def update(self, id: int, dto: BaseDto) -> BaseEntity:
        pass

    @abstractmethod
    async def delete(self, id: int) -> bool:
        pass

    @abstractmethod
    async def count(self) -> int:
        pass
