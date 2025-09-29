from app.src.config import DatabaseConfig
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine


class Adapter:
    def __init__(self, config: DatabaseConfig):
        self._config = config

    def get_engine(self):
        return create_async_engine(url=self._config.get_database_url, echo=True)

    @property
    def get_session(self):
        return async_sessionmaker(self.get_engine(), expire_on_commit=False)
