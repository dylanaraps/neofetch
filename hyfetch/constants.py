import os
from pathlib import Path

CONFIG_PATH = Path.home() / '.config/hyfetch.json'
VERSION = '1.0.7'

# Global color mode default to 8-bit for compatibility
COLOR_MODE = '8bit'

# Obtain terminal size
try:
    TERM_LEN = os.get_terminal_size().columns
except Exception:
    TERM_LEN = 40

