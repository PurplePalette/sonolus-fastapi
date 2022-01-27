# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from src.models.engine import Engine
from src.models.search import Search


class GetEngineListResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    GetEngineListResponse - a model defined in OpenAPI

        pageCount: The pageCount of this GetEngineListResponse.
        items: The items of this GetEngineListResponse.
        search: The search of this GetEngineListResponse.
    """

    pageCount: int
    items: List[Engine]
    search: Search

    @validator("pageCount")
    def pageCount_min(cls, value):
        assert value >= 1
        return value


GetEngineListResponse.update_forward_refs()
