import uvicorn
from sqlalchemy.exc import IntegrityError

from app.src.config.app_config import AppConfig
from app.src.exceptions.exception import (
    EntityDoesNotExistError,
    InvalidOperationError,
    ServiceError,
    InvalidTokenError,
    AuthenticationFailed,
)
from app.src.exceptions.exception_handler import create_exception_handler
from sqlite3 import DataError, IntegrityError
from fastapi import FastAPI, status
from app.src.loggers import AppLogger
from app.src.ui.rest.http.v1 import router as scrapping_request_routes


class Application:
    HOST = "0.0.0.0"

    def __init__(self, logger: AppLogger, config: AppConfig):
        self.__app = FastAPI()
        self.__logger = logger
        self.__config = config
        self.__v1_routes = [scrapping_request_routes]
        self.__exception_handlers = [
            {
                "exception": EntityDoesNotExistError,
                "status_code": status.HTTP_404_NOT_FOUND,
                "detail": "Entity does not exist.",
            },
            {
                "exception": InvalidOperationError,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "detail": "Can't perform the operation.",
            },
            {
                "exception": IntegrityError,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "detail": "Can't process the request due to integrity error.",
            },
            {
                "exception": DataError,
                "status_code": status.HTTP_400_BAD_REQUEST,
                "detail": "Data can't be processed, check the input.",
            },
            {
                "exception": AuthenticationFailed,
                "status_code": status.HTTP_401_UNAUTHORIZED,
                "detail": "Authentication failed due to invalid credentials.",
            },
            {
                "exception": InvalidTokenError,
                "status_code": status.HTTP_401_UNAUTHORIZED,
                "detail": "Invalid token, please re-authenticate.",
            },
            {
                "exception": ServiceError,
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "detail": "A service seems to be down, try again later.",
            },
        ]

    def start(self):
        self.__init_()

        port = self.__config.server_port
        self.__logger.info(f"Starting IOC SCRAPPING API ON ADDRESS {self.HOST}:{port}")
        uvicorn.run(self.__app, host=self.HOST, port=port, log_level="info")

    def __init_(self):
        self.__init__v1_routes()
        self.__init_exception_handler()

    def __init__v1_routes(self):
        prefix = f"/{self.__config.root_prefix}/{self.__config.version_prefix}"
        for route in self.__v1_routes:
            self.__app.include_router(route, prefix=prefix)

    def __init_exception_handler(self):
        for handler in self.__exception_handlers:
            self.__app.add_exception_handler(
                exc_class_or_status_code=handler["exception"],
                handler=create_exception_handler(
                    logger=self.__logger,
                    status_code=handler["status_code"],
                    initial_detail=handler["detail"],
                ),
            )
