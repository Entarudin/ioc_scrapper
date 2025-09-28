from app.src.dtos import CreateScrappingRequestDto
from app.src.repositories.scrapping_request import ScrappingRequestRepository


class ScrappingRequestService:
    def __init__(self, repository: ScrappingRequestRepository):
        self.__repository = repository

    async def create(self, dto: CreateScrappingRequestDto):
        return await self.__repository.create(dto)
