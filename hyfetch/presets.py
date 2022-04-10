from dataclasses import dataclass
from typing import Literal

from .color_util import RGB


@dataclass
class ColorProfile:
    colors: list[str]
    spacing: Literal['equal', 'weighted'] = 'equal'

    def decode(self) -> list[RGB]:
        """
        Decode to a list of RGBs

        :return: List of RGBs
        """
        return [RGB.from_hex(c) for c in self.colors]
