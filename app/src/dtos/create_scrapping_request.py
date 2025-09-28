from pydantic import BaseModel, Field


class CreateScrappingRequestDto(BaseModel):
    type: str = Field(..., min_length=1, description="Тип запроса на скрапинг")
    keyword: str = Field(..., min_length=1, description="Ключевое слово для поиска")

    class Config:
        from_attributes = True
