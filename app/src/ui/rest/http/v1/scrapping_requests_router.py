from fastapi import APIRouter, Query, Path, status
from starlette.responses import JSONResponse

from app.src.builders import ResponseBuilder
from app.src.entities import ScrappingRequestEntity
from app.src.constants import DEFAULT_PAGE, DEFAULT_SIZE

from app.src.dtos import CreateScrappingRequestDto, UpdateScrappingRequestDto
from app.src.container import container

router = APIRouter(prefix="/scrapping_requests", tags=["Scrapping Request"])


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=list[ScrappingRequestEntity]
)
async def get_list(
    page: int = Query(ge=1, default=DEFAULT_PAGE),
    size: int = Query(ge=1, le=DEFAULT_SIZE),
) -> JSONResponse:
    items, qty_items = await container.scrapping_request_service.get_list(page, size)
    return ResponseBuilder.build_paginated_response(items, qty_items, page, size)


@router.get(
    "/{id}", status_code=status.HTTP_200_OK, response_model=ScrappingRequestEntity
)
async def get_by_id(
    id: int = Path(ge=1),
) -> JSONResponse:
    result = await container.scrapping_request_service.get_by_id(id)
    return ResponseBuilder.build(result)


@router.post(
    "/", status_code=status.HTTP_201_CREATED, response_model=ScrappingRequestEntity
)
async def create(
    dto: CreateScrappingRequestDto,
) -> JSONResponse:
    result = await container.scrapping_request_service.create(dto)
    return ResponseBuilder.build(result, status_code=status.HTTP_201_CREATED)


@router.patch(
    "/{id}", status_code=status.HTTP_201_CREATED, response_model=ScrappingRequestEntity
)
async def update(
    dto: UpdateScrappingRequestDto,
    id: int = Path(ge=1),
) -> JSONResponse:
    result = await container.scrapping_request_service.update(id, dto)
    return ResponseBuilder.build(result, status_code=status.HTTP_201_CREATED)


@router.delete("/{id}", status_code=200, response_model=bool)
async def delete(
    id: int = Path(ge=1),
) -> JSONResponse:
    is_deleted = await container.scrapping_request_service.delete(id)
    return ResponseBuilder.build({"success": is_deleted})
