# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class EditEffectRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    EditEffectRequest - a model defined in OpenAPI

        title: The title of this EditEffectRequest [Optional].
        titleEn: The titleEn of this EditEffectRequest [Optional].
        subtitle: The subtitle of this EditEffectRequest [Optional].
        subtitleEn: The subtitleEn of this EditEffectRequest [Optional].
        author: The author of this EditEffectRequest [Optional].
        authorEn: The authorEn of this EditEffectRequest [Optional].
        description: The description of this EditEffectRequest [Optional].
        descriptionEn: The descriptionEn of this EditEffectRequest [Optional].
        thumbnail: The thumbnail of this EditEffectRequest [Optional].
        data: The data of this EditEffectRequest [Optional].
        public: The public of this EditEffectRequest [Optional].
    """

    title: Optional[str] = None
    titleEn: Optional[str] = None
    subtitle: Optional[str] = None
    subtitleEn: Optional[str] = None
    author: Optional[str] = None
    authorEn: Optional[str] = None
    description: Optional[str] = None
    descriptionEn: Optional[str] = None
    thumbnail: Optional[str] = None
    data: Optional[str] = None
    public: Optional[bool] = None

    @validator("title")
    def title_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("title")
    def title_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("titleEn")
    def titleEn_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("subtitle")
    def subtitle_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("subtitle")
    def subtitle_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("subtitleEn")
    def subtitleEn_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("author")
    def author_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("author")
    def author_max_length(cls, value):
        assert len(value) <= 50
        return value

    @validator("authorEn")
    def authorEn_max_length(cls, value):
        assert len(value) <= 50
        return value

    @validator("description")
    def description_max_length(cls, value):
        assert len(value) <= 3000
        return value

    @validator("descriptionEn")
    def descriptionEn_max_length(cls, value):
        assert len(value) <= 3000
        return value


EditEffectRequest.update_forward_refs()
