from __future__ import annotations

from typing import Any

import httpx

from ombala.exceptions import (
    AuthenticationError,
    OmbalaError,
    RateLimitError,
    ServerError,
    ValidationError,
)
from ombala.resources.credits import CreditsResource
from ombala.resources.messages import MessagesResource
from ombala.resources.senders import SendersResource

BASE_URL = "https://api.useombala.ao"


def error(status_code: int, response_data: dict[str, Any] | None) -> OmbalaError:
    message = str(response_data) if response_data else f"HTTP {status_code}"
    if status_code == 401:
        return AuthenticationError(message, status_code, response_data)
    if status_code == 429:
        return RateLimitError(message, status_code, response_data)
    if 400 <= status_code < 500:
        return ValidationError(message, status_code, response_data)
    if 500 <= status_code < 600:
        return ServerError(message, status_code, response_data)
    return OmbalaError(message, status_code, response_data)


class Ombala:
    def __init__(self, token: str, base_url: str = BASE_URL, timeout: int = 30) -> None:
        self._client = httpx.Client(
            base_url=base_url,
            headers={
                "Authorization": f"Token {token}",
                "Content-Type": "application/json",
            },
            timeout=timeout,
        )
        self.messages = MessagesResource(self)
        self.senders = SendersResource(self)
        self.credits = CreditsResource(self)

    def _request(self, method: str, path: str, **kwargs: Any) -> httpx.Response:
        try:
            response = self._client.request(method, path, **kwargs)
        except httpx.HTTPError as exc:
            raise OmbalaError(f"Request failed: {exc}") from exc

        if response.is_error:
            try:
                data = response.json()
            except Exception:
                data = None
            raise error(response.status_code, data)

        return response

    def get(self, path: str, **kwargs: Any) -> httpx.Response:
        return self._request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> httpx.Response:
        return self._request("POST", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> httpx.Response:
        return self._request("DELETE", path, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> Ombala:
        return self

    def __exit__(self, *args: Any) -> None:
        self.close()
