from pydantic import BaseModel


class BaseDto(BaseModel):
    class Config:
        from_attributes = True
