# coding: utf-8

from typing import Dict

import pytest
from httpx import AsyncClient
from src.models.get_background_list_response import (  # noqa: F401
    GetBackgroundListResponse,
)
from src.models.get_background_response import GetBackgroundResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_users_background(client: AsyncClient) -> None:
    """Test case for get_users_background

    Get users background
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/users/{userId}/backgrounds/{backgroundName}".format(
            userId="userId_example", backgroundName="background_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_users_backgrounds(client: AsyncClient) -> None:
    """Test case for get_users_backgrounds

    Get users background list
    """
    params: Dict[str, str] = {
        "localization": "en",
        "page": "0",
        "keywords": "Chino",
        "sort": "0",
        "order": "0",
        "status": "0",
        "author": "any",
        "random": "0",
    }
    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/users/{userId}/backgrounds/list".format(userId="userId_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
