from typing import Any
from abc import ABC

from ..adapters.http.adapter import Adapter as HttpAdapter
from bs4 import BeautifulSoup


class BaseScrapper(ABC):
    def __init__(self, adapter: HttpAdapter):
        self.adapter = adapter

    async def scrape(self, url: str) -> dict[str, Any]:
        soup = await self.__get_soup_by_request(url)
        return soup.__dict__

    async def __get_soup_by_request(self, url: str) -> BeautifulSoup:
        response = await self.adapter.get(url)
        await self.adapter.close()
        soup = BeautifulSoup(response.to_text(), "lxml")
        return soup
