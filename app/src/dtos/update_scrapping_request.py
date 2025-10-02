from typing import Optional

from app.src.dtos.base_dto import BaseDto


class UpdateScrappingRequestDto(BaseDto):
    status: Optional[str]
    data: Optional[dict]
