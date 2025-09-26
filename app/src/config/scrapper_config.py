from .base_config import BaseConfig


class ScrapperConfig(BaseConfig):
    SCRAPPER_VIRUS_TOTAL_BASE_URL_KEY = "SCRAPPER_VIRUS_TOTAL_BASE_URL"

    def get_scrapper_virus_total_base_url(self) -> str:
        return self._get(self.SCRAPPER_VIRUS_TOTAL_BASE_URL_KEY)
