from typing import Optional

from pydantic import Field

from app.src.dtos.base_dto import BaseDto


class CreateScrappingRequestDto(BaseDto):
    type: str = Field(min_length=1, description="Тип запроса на скрапинг")
    keyword: str = Field(min_length=1, description="Ключевое слово для поиска")
    status: Optional[str]
