from functools import cached_property

from .loggers import AppLogger, logger_config
from .adapters.http import Adapter as HttpAdapter


class Container:
    @cached_property
    def app_logger(self) -> AppLogger:
        return AppLogger("app_logger", logger_config)

    @cached_property
    def http_adapter(self) -> HttpAdapter:
        return HttpAdapter(logger=self.app_logger)


container = Container()
