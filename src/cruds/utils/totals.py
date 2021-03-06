import asyncio

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import true
from src.database.objects.background import Background as BackgroundSave
from src.database.objects.effect import Effect as EffectSave
from src.database.objects.engine import Engine as EngineSave
from src.database.objects.level import Level as LevelSave
from src.database.objects.particle import Particle as ParticleSave
from src.database.objects.skin import Skin as SkinSave
from src.models import UserTotalPublish


async def get_total_publish(db: AsyncSession, databaseId: int) -> UserTotalPublish:
    """指定された内部ユーザーIDのユーザーの各要素の投稿数を取得"""
    counts = await asyncio.gather(
        *[
            db.execute(
                select([func.count(obj.id)]).filter(
                    obj.userId == databaseId and obj.public == true()
                )
            )
            for obj in [
                BackgroundSave,
                EffectSave,
                EngineSave,
                LevelSave,
                ParticleSave,
                SkinSave,
            ]
        ]
    )
    results = list(map(lambda c: int(c.scalars().first()), counts))
    return UserTotalPublish(
        backgrounds=results[0],
        effects=results[1],
        engines=results[2],
        particles=results[3],
        levels=results[4],
        skins=results[5],
    )
