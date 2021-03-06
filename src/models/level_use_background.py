# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from src.models.background import Background


class LevelUseBackground(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LevelUseBackground - a model defined in OpenAPI

        useDefault: The useDefault of this LevelUseBackground [Optional].
        item: The item of this LevelUseBackground [Optional].
    """

    useDefault: Optional[bool] = None
    item: Optional[Background] = None


LevelUseBackground.update_forward_refs()
