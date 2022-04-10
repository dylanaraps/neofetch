from dataclasses import dataclass
from typing import Literal


@dataclass
class ColorProfile:
    colors: list[str]
    spacing: Literal['equal', 'weighted'] = 'equal'
