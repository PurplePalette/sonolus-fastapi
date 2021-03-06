# coding: utf-8

from typing import Dict, List  # noqa: F401

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    Path,
    Query,
    Response,
    Security,
)
from src.models.extra_models import TokenModel  # noqa: F401
from src.models.get_background_list_response import GetBackgroundListResponse
from src.models.get_background_response import GetBackgroundResponse
from src.routers.depends import (
    dependsAuthor,
    dependsKeywords,
    dependsLocalization,
    dependsOrder,
    dependsPage,
    dependsPath,
    dependsRandom,
    dependsSort,
    dependsStatus,
)

router = APIRouter()


@router.get(
    "/accounts/{accountKey}/backgrounds/{backgroundName}",
    responses={
        200: {"model": GetBackgroundResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_backgrounds"],
    summary="Get accounts background",
)
async def get_accounts_background(
    accountKey: str = dependsPath,
    backgroundName: str = dependsPath,
) -> GetBackgroundResponse:
    """It returns specified background info.
    It will raise 404 if the background is not registered in this server"""
    ...


@router.get(
    "/accounts/{accountKey}/backgrounds/list",
    responses={
        200: {"model": GetBackgroundListResponse, "description": "OK"},
        404: {"description": "Not Found"},
    },
    tags=["accounts_backgrounds"],
    summary="Get accounts background list",
)
async def get_accounts_backgrounds(
    accountKey: str = dependsPath,
    localization: str = dependsLocalization,
    page: int = dependsPage,
    keywords: str = dependsKeywords,
    sort: int = dependsSort,
    order: int = dependsOrder,
    status: int = dependsStatus,
    author: str = dependsAuthor,
    random: int = dependsRandom,
) -> GetBackgroundListResponse:
    """ユーザー個別用エンドポイント/ 背景一覧を返す"""
    ...
