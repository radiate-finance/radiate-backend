# generated by datamodel-codegen:
#   filename:  createStream.json

from __future__ import annotations

from typing import Any, Dict, Union

from pydantic import BaseModel, Extra


class TokenItem(BaseModel):
    class Config:
        extra = Extra.forbid

    FA12: str


class FA2(BaseModel):
    class Config:
        extra = Extra.forbid

    tokenAddress: str
    tokenId: str


class TokenItem1(BaseModel):
    class Config:
        extra = Extra.forbid

    FA2: FA2


class TokenItem2(BaseModel):
    class Config:
        extra = Extra.forbid

    tez: Dict[str, Any]


class CreateStreamParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    ratePerSecond: str
    receiver: str
    startTime: str
    stopTime: str
    token: Union[TokenItem, TokenItem1, TokenItem2]
