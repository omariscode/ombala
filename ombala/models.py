from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class SendSMSRequest(BaseModel):
    message: str
    from_: str = Field(alias="from", serialization_alias="from")
    to: str
    schedule: str | None = None


class Message(BaseModel):
    id: str
    message: str
    from_: str | None = Field(None, alias="from")
    to: str | None = None
    status: str | None = None
    created_at: datetime | None = Field(None, alias="createdAt")


class SenderCreate(BaseModel):
    name: str


class Sender(BaseModel):
    id: str
    name: str
    status: str | None = None


class CreditBalance(BaseModel):
    balance: float | None = None
    currency: str | None = None


class Recharge(BaseModel):
    id: str | None = None
    amount: float | None = None
    date: str | None = None


class PaginatedResponse(BaseModel):
    data: list[Any]
    page: int | None = None
    total: int | None = None
    total_pages: int | None = None
