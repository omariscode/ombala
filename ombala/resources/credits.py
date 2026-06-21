from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ombala.client import Ombala, AsyncOmbala


class CreditsResource:
    def __init__(self, client: Ombala | AsyncOmbala) -> None:
        self._client = client

    def balance(self) -> dict[str, Any]:
        resp = self._client.get("/v1/credits")
        return resp.json()

    def recharges(self) -> dict[str, Any]:
        resp = self._client.get("/v1/recharges")
        return resp.json()
