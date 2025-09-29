from .base_config import BaseConfig


class AppConfig(BaseConfig):
    SERVICE = "SERVICE"
    APP_ENV = "APP_ENV"
    ROOT_PREFIX = "ROOT"
    VERSION_PREFIX = "VERSION"
    SERVER_PORT = "SERVER_PORT"
    SERVICE_NAME = "SERVICE_NAME"

    @property
    def service_name(self) -> str:
        return self._get(self.SERVICE)

    @property
    def app_env(self) -> str:
        return self._get(self.APP_ENV)

    @property
    def root_prefix(self) -> str:
        return self._get(self.ROOT_PREFIX)

    @property
    def version_prefix(self) -> str:
        return self._get(self.VERSION_PREFIX)

    @property
    def server_port(self) -> int:
        return int(self._get(self.SERVER_PORT))

    @property
    def service_name_prefix(self) -> str:
        return self._get(self.SERVICE_NAME)
