from app.src.dtos import CreateScrappingRequestDto
from app.src.entities.base_entity import BaseEntity
from app.src.enums.scrapper_request_status import ScrapperRequestStatus
from app.src.repositories.scrapping_request import ScrappingRequestRepository
from app.src.services.base_service import BaseService


class ScrappingRequestService(BaseService):
    def __init__(self, repository: ScrappingRequestRepository):
        super().__init__(repository)

    async def create(self, dto: CreateScrappingRequestDto) -> BaseEntity:
        dto.status = ScrapperRequestStatus.PENDING.value
        return await super().create(dto)
