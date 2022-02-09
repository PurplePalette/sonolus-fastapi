# coding: utf-8

from typing import Dict

from httpx import AsyncClient
import pytest
from src.models.get_background_list_response import (  # noqa: F401
    GetBackgroundListResponse,
)
from src.models.get_background_response import GetBackgroundResponse  # noqa: F401


@pytest.mark.asyncio
async def test_get_background_test(client: AsyncClient) -> None:
    """Test case for get_background_test

    Get tests background
    """

    headers: Dict[str, str] = {}
    response = await client.request(
        "GET",
        "/tests/{testId}/backgrounds/{backgroundName}".format(
            testId="testId_example", backgroundName="background_name_example"
        ),
        headers=headers,
    )

    assert response.status_code != 500


@pytest.mark.asyncio
async def test_get_tests_backgrounds(client: AsyncClient) -> None:
    """Test case for get_tests_backgrounds

    Get tests background list
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
        "/tests/{testId}/backgrounds/list".format(testId="testId_example"),
        headers=headers,
        params=params,
    )

    assert response.status_code != 500
