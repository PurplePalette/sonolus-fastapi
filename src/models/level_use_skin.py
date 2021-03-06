# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from src.models.skin import Skin


class LevelUseSkin(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    LevelUseSkin - a model defined in OpenAPI

        useDefault: The useDefault of this LevelUseSkin [Optional].
        item: The item of this LevelUseSkin [Optional].
    """

    useDefault: Optional[bool] = None
    item: Optional[Skin] = None


LevelUseSkin.update_forward_refs()
