from app.src.config import ScrapperConfig
from app.src.dtos import UpdateScrappingRequestDto
from app.src.entities import ScrappingRequestEntity
from app.src.enums import ScrapperType, ScrapperRequestStatus
from app.src.loggers import AppLogger
from app.src.repositories import ScrappingRequestRepository
from app.src.scrappers import ScrapperFactory
from app.src.services import ScrappingRequestService


class ScrapperService:
    def __init__(
        self,
        logger: AppLogger,
        scrapper_config: ScrapperConfig,
        scrapping_request_repository: ScrappingRequestRepository,
        scrapping_request_service: ScrappingRequestService,
        scrapper_factory: ScrapperFactory,
    ):
        self._logger = logger
        self._config = scrapper_config
        self._scrapping_request_repository = scrapping_request_repository
        self._scrapping_request_service = scrapping_request_service
        self._scrapper_factory = scrapper_factory

    async def start_scrapping(self) -> None:
        async for (
            batch
        ) in self._scrapping_request_repository.get_batches_for_scrapping():
            self._logger.info(f"Start scrapping batch with size: {len(batch)}")
            for item in batch:
                await self.scrape(item)

    async def scrape(self, entity: ScrappingRequestEntity) -> None:
        self._logger.info(
            f"Start scrapping entity with keyword: {entity.keyword}, id: {entity.id}"
        )
        try:
            scrapping_source = self.__get_scrapper_source_by_type(entity.type)
            scrapper = self._scrapper_factory.create(scrapping_source)
            scrapping_data = await scrapper.scrape(entity.keyword)
            status = ScrapperRequestStatus.SUCCESS.value
        except Exception as e:
            self._logger.error(
                f"Failed to scrape entity with keyword: {entity.keyword}, id: {entity.id}, error: {"; ".join(e.args)}"
            )
            status = ScrapperRequestStatus.FAILED.value
            scrapping_data = None

        updated_dto = UpdateScrappingRequestDto(status=status, data=scrapping_data)
        await self._scrapping_request_service.update(entity.id, updated_dto)
        self._logger.info(
            f"Finish scrapping entity with keyword: {entity.keyword}, id: {entity.id}"
        )

    def __get_scrapper_source_by_type(self, scrapper_type: str) -> str:
        mapping = {
            ScrapperType.DOMAIN.value: self._config.scrapper_virus_total_base_url
        }
        value = mapping.get(scrapper_type)
        if value is None:
            raise Exception(f"Unknown scrapper type: {scrapper_type}")
        return value
