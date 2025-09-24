import aiohttp
from .response import Response
from ...loggers import AppLogger


class Adapter:
    def __init__(self, *, timeout: int = 10, logger: AppLogger):
        self.timeout = aiohttp.ClientTimeout(total=timeout)
        self.session = aiohttp.ClientSession(timeout=self.timeout)
        self.logger = logger

    async def request(self, method: str, url: str, **kwargs) -> Response:
        self.logger.info(f"HTTP REQUEST: {method.upper()} {url} kwargs={kwargs}")
        async with self.session.request(method, url, **kwargs) as response:
            body = await response.text()
            self.logger.info(f"HTTP RESPONSE: {response.status}, {len(body)} bytes")
            return Response(
                body=body, status=response.status, headers=dict(response.headers)
            )

    async def get(self, url: str, **kwargs) -> Response:
        return await self.request("GET", url, **kwargs)

    async def post(self, url: str, **kwargs) -> Response:
        return await self.request("POST", url, **kwargs)

    async def close(self):
        await self.session.close()
