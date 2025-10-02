from sqlalchemy import JSON, VARCHAR, String
from sqlalchemy.orm import Mapped, mapped_column


from .base_model import BaseModel


class ScrappingRequestModel(BaseModel):
    __tablename__ = "scrapping_requests"

    type: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    status: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    keyword: Mapped[str] = mapped_column(VARCHAR(512), unique=True)
    data: Mapped[dict] = mapped_column(JSON, nullable=True)
