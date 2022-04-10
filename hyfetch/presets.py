from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Optional

from .color_util import RGB


class ColorProfile:
    raw: list[str]
    colors: list[RGB]
    spacing: Literal['equal', 'weighted'] = 'equal'

    def __init__(self, colors: list[str] | list[RGB]):
        if isinstance(colors[0], str):
            self.raw = colors
            self.colors = [RGB.from_hex(c) for c in colors]
        else:
            self.colors = colors


    def with_weights(self, weights: list[int]) -> list[RGB]:
        """
        Map colors based on weights

        :param weights: Weights of each color (weights[i] = how many times color[i] appears)
        :return:
        """
        return [c for i, w in enumerate(weights) for c in [self.colors[i]] * w]

    def with_length(self, length: int) -> list[RGB]:
        """
        Spread to a specific length of text

        :param length: Length of text
        :return: List of RGBs of the length
        """
        preset_len = len(self.colors)
        center_i = preset_len // 2

        # How many copies of each color should be displayed at least?
        repeats = length // preset_len
        weights = [repeats] * preset_len

        # How many extra space left?
        extras = length % preset_len

        # If there is an even space left, extend the center by one space
        if extras % 2 == 1:
            extras -= 1
            weights[center_i] += 1

        # Add weight to border until there's no space left (extras must be even at this point)
        border_i = 0
        while extras > 0:
            extras -= 2
            weights[border_i] += 1
            weights[-(border_i + 1)] += 1
            border_i += 1

        return self.with_weights(weights)

    def color_text(self, txt: str, foreground: bool = True, space_only: bool = False) -> str:
        """
        Color a text

        :param txt: Text
        :param foreground: Whether the foreground text show the color or the background block
        :param space_only: Whether to only color spaces
        :return: Colored text
        """
        colors = self.with_length(len(txt))
        result = ''
        for i, t in enumerate(txt):
            if space_only and t != ' ':
                if i > 0 and txt[i - 1] == ' ':
                    result += '\033[0m'
                result += t
            else:
                result += colors[i].to_ansi_rgb(foreground) + t

        result += '\033[0m'
        return result


PRESETS: dict[str, ColorProfile] = {
    'rainbow': ColorProfile([
        '#E50000',
        '#FF8D00',
        '#FFEE00',
        '#028121',
        '#004CFF',
        '#770088'
    ]),

    'transgender': ColorProfile([
        '#55CDFD',
        '#F6AAB7',
        '#FFFFFF',
        '#F6AAB7',
        '#55CDFD'
    ]),
    'nonbinary': ColorProfile([
        '#FCF431',
        '#FCFCFC',
        '#9D59D2',
        '#282828'
    ]),
    'agender': ColorProfile([
        '#000000',
        '#BABABA',
        '#FFFFFF',
        '#BAF484',
        '#FFFFFF',
        '#BABABA',
        '#000000'
    ]),
    'queer': ColorProfile([
        '#B57FDD',
        '#FFFFFF',
        '#49821E'
    ]),
    'genderfluid': ColorProfile([
        '#FE76A2',
        '#FFFFFF',
        '#BF12D7',
        '#000000',
        '#303CBE'
    ]),

    'bisexual': ColorProfile([
        '#D60270',
        '#9B4F96',
        '#0038A8'
    ]),
    'pansexual': ColorProfile([
        '#FF1C8D',
        '#FFD700',
        '#1AB3FF'
    ]),
    'lesbian': ColorProfile([
        '#D62800',
        '#FF9B56',
        '#FFFFFF',
        '#D462A6',
        '#A40062'
    ]),
    'asexual': ColorProfile([
        '#000000',
        '#A4A4A4',
        '#FFFFFF',
        '#810081'
    ]),
    'aromantic': ColorProfile([
        '#3BA740',
        '#A8D47A',
        '#FFFFFF',
        '#ABABAB',
        '#000000'
    ]),
}
