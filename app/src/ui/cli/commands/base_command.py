from abc import ABC, abstractmethod
from app.src.container import container


class BaseCommand(ABC):
    @abstractmethod
    async def _execute(self):
        pass

    async def execute(self):
        self._pre_execute()
        await self._execute()
        self._post_execute()

    def _pre_execute(self):
        container.app_logger.info(f"Start command {self.__class__.__name__}")

    def _post_execute(self):
        container.app_logger.info(f"Finish command {self.__class__.__name__}")
