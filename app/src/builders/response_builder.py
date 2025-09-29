from typing import List

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import status

from app.src.entities.base_entity import BaseEntity


class ResponseBuilder:
    @staticmethod
    def build(
        data: BaseEntity | dict, status_code: int = status.HTTP_200_OK
    ) -> JSONResponse:
        content = {"data": data}
        return JSONResponse(status_code=status_code, content=jsonable_encoder(content))

    @staticmethod
    def build_paginated_response(
        items: List[BaseEntity], qty_items: int, page: int, size: int
    ) -> JSONResponse:
        content = {
            "data": {"items": items, "total": qty_items, "page": page, "size": size}
        }
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(content)
        )
