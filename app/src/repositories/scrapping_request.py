from abc import ABC, abstractmethod
from typing import AsyncIterator

from app.src.entities.base_entity import BaseEntity
from app.src.repositories.base_repository import BaseRepository


class ScrappingRequestRepository(BaseRepository, ABC):
    @abstractmethod
    async def get_batches_for_scrapping(self) -> AsyncIterator[list[BaseEntity]]:
        pass
