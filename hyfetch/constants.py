from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from typing_extensions import Literal

CONFIG_PATH = Path.home() / '.config/hyfetch.json'
VERSION = '1.0.7'

# Obtain terminal size
try:
    TERM_LEN = os.get_terminal_size().columns
except Exception:
    TERM_LEN = 40

TEST_ASCII = r"""
  |\___/|    
  )     (    
 =\     /=   
   )===(     
  /     \    
  |     |    
 / {txt} \   
 \       /   
_/\_   _/_/\_
|  |( (  |  |
|  | ) ) |  |
|  |(_(  |  |""".strip('\n')

TEST_ASCII_WIDTH = max(len(line) for line in TEST_ASCII.split('\n'))

@dataclass
class GlobalConfig:
    # Global color mode default to 8-bit for compatibility
    color_mode: str
    override_distro: str | None
    debug: bool
    is_light: bool

    def light_dark(self) -> Literal['light', 'dark']:
        return 'light' if self.is_light else 'dark'


GLOBAL_CFG = GlobalConfig(color_mode='8bit', override_distro=None, debug=False, is_light=False)
