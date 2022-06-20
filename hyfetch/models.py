from __future__ import annotations

from dataclasses import dataclass

from typing_extensions import Literal

from .color_util import AnsiMode
from .constants import CONFIG_PATH
from .neofetch_util import ColorAlignment
from .serializer import json_stringify


@dataclass
class Config:
    preset: str
    mode: AnsiMode
    light_dark: Literal['light', 'dark'] = 'dark'
    lightness: float | None = None
    color_align: ColorAlignment = ColorAlignment('horizontal')

    def save(self):
        CONFIG_PATH.parent.mkdir(exist_ok=True, parents=True)
        CONFIG_PATH.write_text(json_stringify(self), 'utf-8')
