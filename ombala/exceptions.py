from typing import Any


class OmbalaError(Exception):
    def __init__(self, message: str, status_code: int | None = None,response_data: dict[str, Any] | None = None) -> None:
        self.status_code = status_code
        self.response_data = response_data
        super().__init__(message)


class AuthenticationError(OmbalaError): ...


class ValidationError(OmbalaError): ...


class RateLimitError(OmbalaError): ...


class ServerError(OmbalaError): ...
