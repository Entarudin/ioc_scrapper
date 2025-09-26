import logging.config
from .settings import logger_config


class AppLogger:
    def __init__(self, name: str, config: dict = None):
        if config is None:
            config = logger_config
        logging.config.dictConfig(config)
        self.__origin = logging.getLogger(name)

    def debug(self, msg, *args, **kwargs):
        return self.__get_origin().debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs):
        return self.__get_origin().info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs):
        return self.__get_origin().warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs):
        return self.__get_origin().error(msg, *args, **kwargs)

    def critical(self, msg, *args, **kwargs):
        return self.__get_origin().critical(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs):
        return self.__get_origin().exception(msg, *args, **kwargs)

    def __get_origin(self) -> logging.Logger:
        return self.__origin
