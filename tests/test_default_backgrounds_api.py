# coding: utf-8

from typing import Dict
from httpx import AsyncClient
import pytest
from src.models.background import Background  # noqa: F401
from src.models.get_background_list_response import (  # noqa: F401
    GetBackgroundListResponse,
)
from src.models.get_background_response import GetBackgroundResponse  # noqa: F401


@pytest.mark.asyncio
async def test_add_background(client: AsyncClient) -> None:
    """Test case for add_background

    Add a background
    """
    add_background_request = {
        "image": "image",
        "thumbnail": "thumbnail",
        "data": "data",
        "configuration": "configuration",
        "author": "author",
        "subtitle": "subtitle",
        "description": "No description",
        "title": "newTitle",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "POST",
        "/backgrounds",
        headers=headers,
        json=add_background_request,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_delete_background(client: AsyncClient) -> None:
    """Test case for delete_background

    Delete a background
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "DELETE",
        "/backgrounds/{backgroundName}".format(
            backgroundName="background_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_edit_background(client: AsyncClient) -> None:
    """Test case for edit_background

    Edit a background
    """
    background = {
        "descriptionEn": "No description",
        "image": {"type": "LevelData", "hash": "hash", "url": "url"},
        "updatedTime": 0,
        "thumbnail": {"type": "LevelData", "hash": "hash", "url": "url"},
        "data": {"type": "LevelData", "hash": "hash", "url": "url"},
        "configuration": {"type": "LevelData", "hash": "hash", "url": "url"},
        "author": "author",
        "description": "No description",
        "title": "title",
        "version": 1,
        "subtitleEn": "subtitleEn",
        "userId": "userId",
        "titleEn": "titleEn",
        "subtitle": "subtitle",
        "name": "name",
        "createdTime": 0,
        "authorEn": "authorEn",
    }

    headers = {
        "Authorization": "Bearer special-key",
    }
    response = await client.request(
        "PATCH",
        "/backgrounds/{backgroundName}".format(
            backgroundName="background_name_example"
        ),
        headers=headers,
        json=background,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_background(client: AsyncClient) -> None:
    """Test case for get_background

    Get a background
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/backgrounds/{backgroundName}".format(backgroundName="4dwhzidtjpda"),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_background_list(client: AsyncClient) -> None:
    """Test case for get_background_list

    Get background list
    """
    params: Dict[str, str] = {
        "localization": "en",
        "page": "0",
        "keywords": "Chino",
        "sort": "updated_time",
        "order": "desc",
        "status": "any",
        "author": "any",
        "random": "0",
    }
    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/backgrounds/list",
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
