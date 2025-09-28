from app.src.dtos import CreateScrappingRequestDto
from app.src.enums.scrapper_request_status import ScrapperRequestStatus
from app.src.models import ScrappingRequestModel
from app.src.repositories.scrapping_request import ScrappingRequestRepository
from app.src.adapters.sqlalchemy import Adapter as SQLAlchemyAdapter


class PgScrappingRequestRepository(ScrappingRequestRepository):
    def __init__(self, adapter: SQLAlchemyAdapter):
        self.__adapter = adapter

    async def create(self, dto: CreateScrappingRequestDto):
        async with self.__adapter.get_session() as session:
            model = ScrappingRequestModel(
                type=dto.type,
                keyword=dto.keyword,
                status=ScrapperRequestStatus.PENDING.value,
            )
            session.add(model)
            await session.commit()
            return model
