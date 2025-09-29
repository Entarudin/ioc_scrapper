from typing import Optional

from app.src.entities.base_entity import BaseEntity


class ScrappingRequestEntity(BaseEntity):
    type: str
    status: str
    keyword: str
    data: Optional[dict]
