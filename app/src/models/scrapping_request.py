from sqlalchemy import JSON, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column


from .base_model import BaseModel


class ScrappingRequestModel(BaseModel):
    __tablename__ = "scrapping_requests"

    type: Mapped[str] = mapped_column(VARCHAR)
    status: Mapped[str] = mapped_column(VARCHAR)
    keyword: Mapped[str] = mapped_column(VARCHAR)
    data: Mapped[dict] = mapped_column(JSON, nullable=True)
