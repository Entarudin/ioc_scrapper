from functools import cached_property

from .loggers import AppLogger, logger_config
from .adapters.http import Adapter as HttpAdapter
from .adapters.sqlalchemy import Adapter as SqlAdapter
from .config import ScrapperConfig, DatabaseConfig
from .repositories.postres import PgScrappingRequestRepository
from .repositories.scrapping_request import ScrappingRequestRepository
from .scrappers import VirusTotalScrapper, ScrapperFactory
from .services import ScrappingRequestService


class Container:
    @cached_property
    def app_logger(self) -> AppLogger:
        return AppLogger("app_logger", logger_config)

    @cached_property
    def http_adapter(self) -> HttpAdapter:
        return HttpAdapter(logger=self.app_logger)

    @cached_property
    def scrapper_config(self) -> ScrapperConfig:
        return ScrapperConfig()

    @cached_property
    def get_database_config(self) -> DatabaseConfig:
        return DatabaseConfig()

    @cached_property
    def get_sqlalchemy_adapter(self) -> SqlAdapter:
        return SqlAdapter(config=self.get_database_config)

    @cached_property
    def get_scrapping_request_service(self) -> ScrappingRequestService:
        return ScrappingRequestService(self.get_scrapping_request_repository)

    @cached_property
    def get_scrapping_request_repository(self) -> ScrappingRequestRepository:
        return PgScrappingRequestRepository(self.get_sqlalchemy_adapter)

    @cached_property
    def get_virus_total_scrapper(self) -> VirusTotalScrapper:
        return VirusTotalScrapper(
            adapter=self.http_adapter,
            base_url=self.scrapper_config.scrapper_virus_total_base_url,
        )

    @cached_property
    def get_scrappers_factory(self) -> ScrapperFactory:
        return ScrapperFactory(
            {
                self.scrapper_config.scrapper_virus_total_base_url: self.get_virus_total_scrapper
            }
        )


container = Container()
