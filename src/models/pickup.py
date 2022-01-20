# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Pickup(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Pickup - a model defined in OpenAPI

        level_name: The level_name of this Pickup.
        order: The order of this Pickup.
    """

    level_name: str
    order: int

    @validator("order")
    def order_max(cls, value):
        assert value <= 99999
        return value

    @validator("order")
    def order_min(cls, value):
        assert value >= 10000
        return value


Pickup.update_forward_refs()
