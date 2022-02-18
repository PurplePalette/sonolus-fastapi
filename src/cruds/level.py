import asyncio
from dataclasses import dataclass
from typing import Any, Dict, Union

from fastapi import HTTPException
from fastapi_cloudauth.firebase import FirebaseClaims
from fastapi_pagination import Page, Params
from fastapi_pagination.ext.async_sqlalchemy import paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload
from src.cruds.abstract import AbstractCrud
from src.cruds.search import buildDatabaseQuery
from src.cruds.utils import (
    db_to_resp,
    get_current_unix,
    get_first_item_or_404,
    get_new_name,
    is_owner_or_admin_otherwise_409,
    patch_to_model,
    req_to_db,
    save_to_db,
)
from src.database.objects import (
    BackgroundSave,
    EffectSave,
    EngineSave,
    GenreSave,
    LevelSave,
    ParticleSave,
    SkinSave,
)
from src.models.add_level_request import AddLevelRequest
from src.models.default_search import defaultSearch
from src.models.edit_level_request import EditLevelRequest
from src.models.get_level_list_response import GetLevelListResponse
from src.models.get_level_response import GetLevelResponse
from src.models.level import Level as LevelReqResp
from src.models.search_query import SearchQueries
from src.models.sonolus_page import SonolusPage, toSonolusPage


@dataclass
class SRLConvert:
    obj: Any
    name: str


SRLConvertDict = [
    SRLConvert(EngineSave, "engine"),
    SRLConvert(BackgroundSave, "background"),
    SRLConvert(EffectSave, "effect"),
    SRLConvert(SkinSave, "skin"),
    SRLConvert(ParticleSave, "particle"),
    SRLConvert(GenreSave, "genre"),
]


class LevelCrud(AbstractCrud):  # type: ignore
    async def create_dict(
        self, db: AsyncSession, model: LevelReqResp, exclude_unset: bool = False
    ) -> Dict[str, Any]:
        """モデルに指定されたSonolusオブジェクトをDBから取り出してIDを埋めます"""
        model_import: Dict[str, Any] = model.dict(exclude_unset=exclude_unset)
        # DB側カラム名に合わせる
        if "artists" in model_import:
            model_import["subtitle"] = model_import["artists"]
        if "artistsEn" in model_import:
            model_import["subtitleEn"] = model_import["artistsEn"]
        # SRL周りをDB側のIDに変換
        for convert in SRLConvertDict:
            if convert.name in model_import:
                obj_req = model_import[convert.name]
                if obj_req:
                    obj_db = await get_first_item_or_404(
                        db, select(convert.obj.id).filter(convert.obj.name == obj_req)
                    )
                    model_import[convert.name + "Id"] = obj_db
        # 存在してると変換できないフィールドを消す
        for key in ["artists", "artistsEn", "preview"] + [
            s.name for s in SRLConvertDict
        ]:
            if key in model_import:
                del model_import[key]
        return model_import

    async def get_single_level(
        self, stmt: Any, db: AsyncSession, localization: str
    ) -> LevelReqResp:
        # 保存するとリレーション周りのデータが消し飛ぶのでjoinedして取得し直す
        level_db: LevelSave = await get_first_item_or_404(
            db,
            stmt.options(
                joinedload(LevelSave.engine).options(
                    joinedload(EngineSave.background),
                    joinedload(EngineSave.skin),
                    joinedload(EngineSave.particle),
                    joinedload(EngineSave.effect),
                ),
                joinedload(LevelSave.particle),
                joinedload(LevelSave.effect),
                joinedload(LevelSave.background),
                joinedload(LevelSave.skin),
                joinedload(LevelSave.genre),
                selectinload(LevelSave.likes),
                selectinload(LevelSave.favorites),
            ),
        )
        # 各地のSRLを応答型に変換し回る
        for db_obj in [
            level_db,
            level_db.engine,
            level_db.engine.skin,
            level_db.engine.background,
            level_db.engine.particle,
            level_db.engine.effect,
        ]:
            await db_to_resp(db, db_obj, localization)
        item = level_db.toLevelItem()
        return item

    async def add(
        self, db: AsyncSession, model: AddLevelRequest, auth: FirebaseClaims
    ) -> Union[HTTPException, GetLevelResponse]:
        """レベルを追加します"""
        model_import = await self.create_dict(db, model)
        level_db = LevelSave(**model_import)
        level_db.name = await get_new_name(db, LevelSave)
        level_db.userId = auth["user_id"]
        await req_to_db(db, level_db, is_new=True)
        await save_to_db(db, level_db)
        item = await self.get_single_level(
            select(LevelSave).filter(LevelSave.id == level_db.id), db, "ja"
        )
        resp = GetLevelResponse(
            item=item,
            description=item.description,
            recommended=[],
        )
        return resp

    async def get(
        self, db: AsyncSession, name: str, localization: str
    ) -> GetLevelResponse:
        """レベルを取得します"""
        item = await self.get_single_level(
            select(LevelSave).filter(LevelSave.name == name), db, localization
        )
        return GetLevelResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def edit(
        self,
        db: AsyncSession,
        name: str,
        model: EditLevelRequest,
        auth: FirebaseClaims,
    ) -> Union[HTTPException, GetLevelResponse]:
        """レベルを編集します"""
        level_db: LevelSave = await get_first_item_or_404(
            db,
            select(LevelSave).filter(
                LevelSave.name == name,
            ),
        )
        await is_owner_or_admin_otherwise_409(db, level_db, auth)
        model_import = await self.create_dict(db, model, True)
        patch_to_model(level_db, model_import)
        await save_to_db(db, level_db)
        item = await self.get_single_level(
            select(LevelSave).filter(LevelSave.id == level_db.id), db, "ja"
        )
        return GetLevelResponse(
            item=item,
            description=item.description,
            recommended=[],
        )

    async def delete(
        self,
        db: AsyncSession,
        name: str,
        auth: FirebaseClaims,
    ) -> Union[HTTPException, None]:
        """レベルを削除します"""
        level_db: LevelSave = await get_first_item_or_404(
            db, select(LevelSave).filter(LevelSave.name == name)
        )
        await is_owner_or_admin_otherwise_409(db, level_db, auth)
        level_db.isDeleted = True
        level_db.updatedTime = get_current_unix()
        await save_to_db(db, level_db)
        return None

    async def list(
        self, db: AsyncSession, page: int, queries: SearchQueries
    ) -> GetLevelListResponse:
        """レベル一覧を取得します"""
        select_query = buildDatabaseQuery(LevelSave, queries)
        userPage: Page[LevelSave] = await paginate(
            db,
            select_query,
            Params(page=page + 1, size=20),
        )  # type: ignore
        resp: SonolusPage = toSonolusPage(userPage)
        await asyncio.gather(
            *[db_to_resp(db, r, queries.localization) for r in resp.items]
        )
        return GetLevelListResponse(
            pageCount=resp.pageCount if resp.pageCount > 0 else 1,
            items=resp.items,
            search=defaultSearch,
        )
