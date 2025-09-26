from .base_scrapper import BaseScrapper


class ScrapperFactory:
    def __init__(self, scrappers: dict[str, BaseScrapper]):
        self.__scrappers = scrappers

    def create(self, url: str) -> BaseScrapper:
        scrapper = self.__scrappers.get(url)
        if scrapper is None:
            raise Exception(f"Scrapper {url} not found")
        return scrapper
