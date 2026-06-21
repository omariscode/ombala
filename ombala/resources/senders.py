from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from ombala.client import Ombala, AsyncOmbala


class SendersResource:
    def __init__(self, client: Ombala | AsyncOmbala) -> None:
        self._client = client

    def create(self, name: str) -> dict[str, Any]:
        resp = self._client.post("/v1/senders/", json={"name": name})
        return resp.json()

    def list(self) -> dict[str, Any]:
        resp = self._client.get("/v1/senders")
        return resp.json()

    def list_approved(self) -> dict[str, Any]:
        resp = self._client.get("/v1/senders/approved")
        return resp.json()

    def list_pending(self) -> dict[str, Any]:
        resp = self._client.get("/v1/senders/pending")
        return resp.json()

    def delete(self, sender_id: str) -> None:
        self._client.delete(f"/v1/senders/{sender_id}")
