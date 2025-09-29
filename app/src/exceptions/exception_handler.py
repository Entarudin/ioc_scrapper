from typing import Callable, Any, Coroutine
from starlette.requests import Request
from starlette.responses import JSONResponse

from .exception import ApiError
from ..loggers import AppLogger


def create_exception_handler(
    logger: AppLogger,
    status_code: int,
    initial_detail: str,
) -> Callable[[Request, ApiError], JSONResponse]:
    detail = {"message": initial_detail}

    async def exception_handler(_: Request, exc: ApiError) -> JSONResponse:
        if exc.message:
            detail["message"] = exc.message

        if exc.name:
            detail["message"] = f"{detail['message']} [{exc.name}]"

        logger.error(exc)
        return JSONResponse(
            status_code=status_code, content={"detail": detail["message"]}
        )

    return exception_handler
