from dotenv import dotenv_values
from abc import ABC


class BaseConfig(ABC):
    def __init__(self):
        self.config = dotenv_values()

    def _get(self, key, default=None):
        value = self.config.get(key, default)
        if value is None:
            raise KeyError(f"Key '{key}' not found in config")
        return value
