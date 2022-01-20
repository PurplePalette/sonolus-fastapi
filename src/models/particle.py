# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401
from src.models.sonolus_resource_locator import SonolusResourceLocator


class Particle(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Particle - a model defined in OpenAPI

        name: The name of this Particle [Optional].
        version: The version of this Particle [Optional].
        title: The title of this Particle [Optional].
        subtitle: The subtitle of this Particle [Optional].
        author: The author of this Particle [Optional].
        thumbnail: The thumbnail of this Particle [Optional].
        data: The data of this Particle [Optional].
        texture: The texture of this Particle [Optional].
        user_id: The user_id of this Particle [Optional].
        created_time: The created_time of this Particle [Optional].
        updated_time: The updated_time of this Particle [Optional].
        description: The description of this Particle [Optional].
    """

    name: Optional[str] = None
    version: Optional[int] = None
    title: Optional[str] = None
    subtitle: Optional[str] = None
    author: Optional[str] = None
    thumbnail: Optional[SonolusResourceLocator] = None
    data: Optional[SonolusResourceLocator] = None
    texture: Optional[SonolusResourceLocator] = None
    user_id: Optional[str] = None
    created_time: Optional[int] = None
    updated_time: Optional[int] = None
    description: Optional[str] = None

    @validator("name")
    def name_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("name")
    def name_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("version")
    def version_max(cls, value):
        assert value <= 100
        return value

    @validator("version")
    def version_min(cls, value):
        assert value >= 1
        return value

    @validator("title")
    def title_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("title")
    def title_max_length(cls, value):
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

    @validator("author")
    def author_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("author")
    def author_max_length(cls, value):
        assert len(value) <= 50
        return value

    @validator("user_id")
    def user_id_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("user_id")
    def user_id_max_length(cls, value):
        assert len(value) <= 100
        return value

    @validator("created_time")
    def created_time_min(cls, value):
        assert value >= 0
        return value

    @validator("updated_time")
    def updated_time_min(cls, value):
        assert value >= 0
        return value

    @validator("description")
    def description_min_length(cls, value):
        assert len(value) >= 1
        return value

    @validator("description")
    def description_max_length(cls, value):
        assert len(value) <= 3000
        return value


Particle.update_forward_refs()
