from fastapi import APIRouter, HTTPException

from app.src.dtos import CreateScrappingRequestDto
from app.src.container import container

router = APIRouter()


@router.post("/scrapping_requests/", status_code=201)
async def create(
    dto: CreateScrappingRequestDto,
):
    service = container.get_scrapping_request_service
    return await service.create(dto)
