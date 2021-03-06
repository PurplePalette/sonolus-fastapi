from dataclasses import dataclass
from typing import List

from src.config import (
    BACKGROUND_VERSION,
    EFFECT_VERSION,
    ENGINE_VERSION,
    LEVEL_VERSION,
    PARTICLE_VERSION,
    SKIN_VERSION,
)


@dataclass
class SRLDefine:
    obj_name: str
    obj_version: int
    locators: List[str]


@dataclass
class SRLDict:
    background: SRLDefine
    effect: SRLDefine
    engine: SRLDefine
    level: SRLDefine
    particle: SRLDefine
    skin: SRLDefine
    announce: SRLDefine


ENGINE_LOCATORS = ["thumbnail", "data", "configuration"]
BACKGROUND_LOCATORS = ["thumbnail", "data", "image", "configuration"]
EFFECT_LOCATORS = ["thumbnail", "data"]
LEVEL_LOCATORS = ["cover", "bgm", "data"]
ANNOUNCE_LOCATORS = ["cover", "bgm"]
PARTICLE_LOCATORS = ["thumbnail", "data", "texture"]
SKIN_LOCATORS = ["thumbnail", "data", "texture"]


SRL_BRIDGES = SRLDict(
    SRLDefine("background", BACKGROUND_VERSION, BACKGROUND_LOCATORS),
    SRLDefine("effect", EFFECT_VERSION, EFFECT_LOCATORS),
    SRLDefine("engine", ENGINE_VERSION, ENGINE_LOCATORS),
    SRLDefine("level", LEVEL_VERSION, LEVEL_LOCATORS),
    SRLDefine("particle", PARTICLE_VERSION, PARTICLE_LOCATORS),
    SRLDefine("skin", SKIN_VERSION, SKIN_LOCATORS),
    SRLDefine("announce", LEVEL_VERSION, ANNOUNCE_LOCATORS),
)
