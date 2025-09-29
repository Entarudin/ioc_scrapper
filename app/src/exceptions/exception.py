class ApiError(Exception):
    """base exception class"""

    def __init__(self, message: str = "Service is unavailable", name: str = ""):
        self.message = message
        self.name = name
        super().__init__(self.message, self.name)


class ServiceError(ApiError):
    """failures in external services or APIs, like a database or a third-party service"""

    pass


class EntityDoesNotExistError(ApiError):
    """database returns nothing"""

    pass


class EntityAlreadyExistsError(ApiError):
    """conflict detected, like trying to create a resource that already exists"""

    pass


class InvalidOperationError(ApiError):
    """invalid operations like trying to delete a non-existing entity, etc."""

    pass


class AuthenticationFailed(ApiError):
    """invalid authentication credentials"""

    pass


class InvalidTokenError(ApiError):
    """invalid token"""

    pass
