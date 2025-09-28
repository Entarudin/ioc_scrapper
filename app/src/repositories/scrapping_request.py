from abc import ABC, abstractmethod

from app.src.dtos import CreateScrappingRequestDto


class ScrappingRequestRepository(ABC):
    @abstractmethod
    async def create(self, dto: CreateScrappingRequestDto):
        pass
