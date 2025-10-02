from .base_config import BaseConfig


class DatabaseConfig(BaseConfig):
    POSTGRES_HOST = "POSTGRES_HOST"
    POSTGRES_PORT = "POSTGRES_PORT"
    POSTGRES_USER = "POSTGRES_USER"
    POSTGRES_PASSWORD = "POSTGRES_PASSWORD"
    POSTGRES_DATABASE = "POSTGRES_DATABASE"

    @property
    def database_url(self):
        return (
            f"postgresql+asyncpg://{self._get(self.POSTGRES_USER)}:{self._get(self.POSTGRES_PASSWORD)}@"
            f"{self._get(self.POSTGRES_HOST)}:{self._get(self.POSTGRES_PORT)}/{self._get(self.POSTGRES_DATABASE)}"
        )
