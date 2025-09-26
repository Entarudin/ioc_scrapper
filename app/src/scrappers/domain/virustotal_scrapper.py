from ...scrappers import BaseScrapper


class VirusTotalScrapper(BaseScrapper):
    def _prepare_url(self, keyword: str) -> str:
        return f"{self.base_url}/gui/ip-address/{keyword}"
