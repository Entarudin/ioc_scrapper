from typing import Any
from abc import ABC, abstractmethod

from ..adapters.http.adapter import Adapter as HttpAdapter
from bs4 import BeautifulSoup


class BaseScrapper(ABC):
    def __init__(self, adapter: HttpAdapter, base_url: str):
        self.adapter = adapter
        self.base_url = base_url

    @abstractmethod
    def _prepare_url(self, keyword: str) -> str:
        pass

    async def scrape(self, keyword: str) -> dict[str, Any]:
        soup = await self.__get_soup_by_request(self._prepare_url(keyword))
        return soup.__dict__

    async def __get_soup_by_request(self, uri: str) -> BeautifulSoup:
        response = await self.adapter.get(uri)
        await self.adapter.close()
        soup = BeautifulSoup(response.to_text(), "lxml")
        return soup
