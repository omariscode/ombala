from __future__ import annotations

from typing import TYPE_CHECKING, Any

from ombala.models import SendSMSRequest

if TYPE_CHECKING:
    from ombala.client import Ombala


class MessagesResource:
    def __init__(self, client: Ombala) -> None:
        self._client = client

    def send(self, message: str, from_: str,to: str, schedule: str | None = None) -> dict[str, Any]:
        body = SendSMSRequest(message=message, from_=from_, to=to, schedule=schedule)
        resp = self._client.post(
            "/v1/messages",
            content=body.model_dump_json(by_alias=True),
        )
        return resp.json()

    def list(self, page: int | None = None) -> dict[str, Any]:
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        resp = self._client.get("/v1/messages", params=params)
        return resp.json()

    def get(self, message_id: str, id: str | None = None) -> dict[str, Any]:
        params: dict[str, Any] = {"message_id": message_id}
        if id is not None:
            params["id"] = id
        resp = self._client.get("/v1/messages/one", params=params)
        return resp.json()

    def delete(self, message_id: str) -> None:
        self._client.delete(f"/v1/messages/{message_id}")

    def list_recipients(
        self,
        page: int | None = None,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        resp = self._client.get("/v1/messages/recipients", params=params)
        return resp.json()

    def list_by_date_range(
        self,
        start: str,
        end: str,
        page: int | None = None,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {"start": start, "end": end}
        if page is not None:
            params["page"] = page
        resp = self._client.get("/v1/messages/date", params=params)
        return resp.json()

    def list_by_recipient(
        self,
        phone_number: str | None = None,
        page: int | None = None,
    ) -> dict[str, Any]:
        params: dict[str, Any] = {}
        if phone_number is not None:
            params["phone_number"] = phone_number
        if page is not None:
            params["page"] = page
        resp = self._client.get("/v1/messages/recipient", params=params)
        return resp.json()
