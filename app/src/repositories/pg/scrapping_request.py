from app.src.entities import ScrappingRequestEntity
from app.src.entities.base_entity import BaseEntity
from app.src.models import BaseModel, ScrappingRequestModel
from app.src.repositories.pg.base_pg_repository import BasePgRepository
from app.src.repositories.scrapping_request import ScrappingRequestRepository
from app.src.adapters.sqlalchemy import Adapter as SQLAlchemyAdapter


class PgScrappingRequestRepository(BasePgRepository, ScrappingRequestRepository):
    def __init__(self, adapter: SQLAlchemyAdapter):
        super().__init__(adapter)

    def _get_model_type(self) -> type[BaseModel]:
        return ScrappingRequestModel

    def _get_entity_type(self) -> type[BaseEntity]:
        return ScrappingRequestEntity
