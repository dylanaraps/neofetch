from __future__ import annotations

import colorsys
from dataclasses import dataclass, astuple
from typing_extensions import Literal

from .constants import GLOBAL_CFG

AnsiMode = Literal['default', 'ansi', '8bit', 'rgb']
LightDark = Literal['light', 'dark']


MINECRAFT_COLORS = ["&0/\033[0;30m", "&1/\033[0;34m", "&2/\033[0;32m", "&3/\033[0;36m", "&4/\033[0;31m",
                    "&5/\033[0;35m", "&6/\033[0;33m", "&7/\033[0;37m", "&8/\033[1;30m", "&9/\033[1;34m",
                    "&a/\033[1;32m", "&b/\033[1;36m", "&c/\033[1;31m", "&d/\033[1;35m", "&e/\033[1;33m",
                    "&f/\033[1;37m",
                    "&r/\033[0m", "&l/\033[1m", "&o/\033[3m", "&n/\033[4m", "&-/\n"]
MINECRAFT_COLORS = [(r[:2], r[3:]) for r in MINECRAFT_COLORS]


def color(msg: str) -> str:
    """
    Replace extended minecraft color codes in string
    :param msg: Message with minecraft color codes
    :return: Message with escape codes
    """
    for code, esc in MINECRAFT_COLORS:
        msg = msg.replace(code, esc)

    while '&gf(' in msg or '&gb(' in msg:
        i = msg.index('&gf(') if '&gf(' in msg else msg.index('&gb(')
        end = msg.index(')', i)
        code = msg[i + 4:end]
        fore = msg[i + 2] == 'f'

        if code.startswith('#'):
            rgb = tuple(int(code.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
        else:
            code = code.replace(',', ' ').replace(';', ' ').replace('  ', ' ')
            rgb = tuple(int(c) for c in code.split(' '))

        msg = msg[:i] + RGB(*rgb).to_ansi(foreground=fore) + msg[end + 1:]

    return msg


def printc(msg: str):
    """
    Print with color
    :param msg: Message with minecraft color codes
    """
    print(color(msg + '&r'))


def clear_screen(title: str = ''):
    """
    Clear screen using ANSI escape codes
    """
    if not GLOBAL_CFG.debug:
        print('\033[2J\033[H', end='')

    if title:
        print()
        printc(title)
        print()


def redistribute_rgb(r: int, g: int, b: int) -> tuple[int, int, int]:
    """
    Redistribute RGB after lightening

    Credit: https://stackoverflow.com/a/141943/7346633
    """
    threshold = 255.999
    m = max(r, g, b)
    if m <= threshold:
        return int(r), int(g), int(b)
    total = r + g + b
    if total >= 3 * threshold:
        return int(threshold), int(threshold), int(threshold)
    x = (3 * threshold - total) / (3 * m - total)
    gray = threshold - x * m
    return int(gray + x * r), int(gray + x * g), int(gray + x * b)


@dataclass(unsafe_hash=True)
class HSL:
    h: float
    s: float
    l: float

    def __iter__(self):
        return iter(astuple(self))

    def rgb(self) -> RGB:
        return RGB(*[round(v * 255.0) for v in colorsys.hls_to_rgb(self.h, self.l, self.s)])


@dataclass(unsafe_hash=True)
class RGB:
    r: int
    g: int
    b: int

    def __iter__(self):
        return iter(astuple(self))

    @classmethod
    def from_hex(cls, hex: str) -> "RGB":
        """
        Create color from hex code

        >>> RGB.from_hex('#FFAAB7')
        RGB(r=255, g=170, b=183)

        :param hex: Hex color code
        :return: RGB object
        """
        hex = hex.lstrip("#")
        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)
        return cls(r, g, b)

    def to_ansi_rgb(self, foreground: bool = True) -> str:
        """
        Convert RGB to ANSI TrueColor (RGB) Escape Code.

        This uses the 24-bit color encoding (an uint8 for each color value), and supports 16 million
        colors. However, not all terminal emulators support this escape code. (For example, IntelliJ
        debug console doesn't support it).

        Currently, we do not know how to detect whether a terminal environment supports ANSI RGB. If
        you have any thoughts, feel free to submit an issue on our Github page!

        :param foreground: Whether the color is for foreground text or background color
        :return: ANSI RGB escape code like \033[38;2;255;100;0m
        """
        c = '38' if foreground else '48'
        return f'\033[{c};2;{self.r};{self.g};{self.b}m'

    def to_ansi_8bit(self, foreground: bool = True) -> str:
        """
        Convert RGB to ANSI 8bit 256 Color Escape Code.

        This encoding supports 256 colors in total.

        :return: ANSI 256 escape code like \033[38;5;206m'
        """
        r, g, b = self.r, self.g, self.b
        sep = 42.5

        while True:
            if r < sep or g < sep or b < sep:
                gray = r < sep and g < sep and b < sep
                break
            sep += 42.5

        if gray:
            color = 232 + (r + g + b) / 33
        else:
            color = 16 + int(r / 256. * 6) * 36 + int(g / 256. * 6) * 6 + int(b / 256. * 6)

        c = '38' if foreground else '48'
        return f'\033[{c};5;{int(color)}m'

    def to_ansi_16(self, foreground: bool = True) -> str:
        """
        Convert RGB to ANSI 16 Color Escape Code

        :return: ANSI 16 escape code
        """
        raise NotImplementedError()

    def to_ansi(self, mode: AnsiMode | None = None, foreground: bool = True):
        if not mode:
            mode = GLOBAL_CFG.color_mode
        if mode == 'rgb':
            return self.to_ansi_rgb(foreground)
        if mode == '8bit':
            return self.to_ansi_8bit(foreground)
        if mode == 'ansi':
            return self.to_ansi_16(foreground)

    def lighten(self, multiplier: float) -> 'RGB':
        """
        Lighten the color by a multiplier

        :param multiplier: Multiplier
        :return: Lightened color (original isn't modified)
        """
        return RGB(*redistribute_rgb(*[v * multiplier for v in self]))

    def hsl(self) -> HSL:
        h, l, s = colorsys.rgb_to_hls(*[v / 255.0 for v in self])
        return HSL(h, s, l)

    def set_light(self, light: float, at_least: bool | None = None, at_most: bool | None = None) -> 'RGB':
        """
        Set HSL lightness value

        :param light: Lightness value (0-1)
        :param at_least: Set the lightness to at least this value (no change if greater)
        :param at_most: Set the lightness to at most this value (no change if lesser)
        :return: New color (original isn't modified)
        """
        # Convert to HSL
        hsl = self.hsl()

        # Modify light value
        if at_least is None and at_most is None:
            hsl.l = light
        else:
            if at_most:
                hsl.l = min(hsl.l, light)
            if at_least:
                hsl.l = max(hsl.l, light)

        # Convert back to RGB
        return hsl.rgb()

    def is_light(self):
        return self.hsl().l > 0.5
