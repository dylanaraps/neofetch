from __future__ import annotations

from dataclasses import dataclass

from typing_extensions import Literal

from .color_util import AnsiMode, LightDark
from .constants import CONFIG_PATH
from .neofetch_util import ColorAlignment
from .serializer import json_stringify, from_dict


@dataclass
class Config:
    preset: str
    mode: AnsiMode
    light_dark: LightDark = 'dark'
    lightness: float | None = None
    color_align: ColorAlignment = ColorAlignment('horizontal')

    @classmethod
    def from_dict(cls, d: dict):
        d['color_align'] = ColorAlignment.from_dict(d['color_align'])
        return from_dict(cls, d)

    def save(self):
        CONFIG_PATH.parent.mkdir(exist_ok=True, parents=True)
        CONFIG_PATH.write_text(json_stringify(self), 'utf-8')
