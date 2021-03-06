# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class AddUserRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    AddUserRequest - a model defined in OpenAPI

        userId: The userId of this AddUserRequest.
    """

    userId: str

    @validator("userId")
    def userId_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("userId")
    def userId_max_length(cls, value):
        assert len(value) <= 30
        return value


AddUserRequest.update_forward_refs()
