# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from enum import Enum
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import Field, BaseModel, Extra  # noqa: F401


class OrderOutput(BaseModel):

    class Config: # was not included in OpenAPI contract, but necessary
        extra = Extra.forbid

    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    OrderOutput - a model defined in OpenAPI

        id: The id of this OrderOutput [Optional].
        stoks: The stoks of this OrderOutput [Optional].
        quantity: The quantity of this OrderOutput [Optional].
        status: The status of this OrderOutput [Optional].
    """

    id: Optional[str] = Field(alias="id", default=None)
    stoks: Optional[str] = Field(alias="stoks", default=None)
    quantity: Optional[float] = Field(alias="quantity", default=None)
    status: Optional['StatusEnum'] = Field(alias="status", default=None)

    @staticmethod
    def from_dict(db_data: dict) -> OrderOutput:
        return OrderOutput(
            id=db_data.get('id'),
            stoks=db_data.get('stoks'),
            quantity=db_data.get('quantity'),
            status=db_data.get('status'),
        )


class StatusEnum(Enum):
    pending = "pending"
    executed = "executed"
    canceled = "canceled"


OrderOutput.model_rebuild()
