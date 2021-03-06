# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator  # noqa: F401


class SearchSelectOption(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    SearchSelectOption - a model defined in OpenAPI

        query: The query of this SearchSelectOption.
        name: The name of this SearchSelectOption.
        type: The type of this SearchSelectOption.
        def: The default of this SearchSelectOption.
        values: The values of this SearchSelectOption.
    """

    query: str
    name: str
    type: str
    default: int
    values: List[str]

    @validator("default")
    def default_min(cls, value):
        assert value >= 0
        return value

    class Config:
        fields = {"default": "def"}
        allow_population_by_field_name = True


SearchSelectOption.update_forward_refs()
