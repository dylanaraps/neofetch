from __future__ import annotations

from typing import Iterable

from typing_extensions import Literal

from .color_util import RGB, LightDark
from .constants import GLOBAL_CFG


def remove_duplicates(seq: Iterable) -> list:
    """
    Remove duplicate items from a sequence while preserving the order
    """
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


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
                result += colors[i].to_ansi(foreground=foreground) + t

        result += '\033[0m'
        return result

    def lighten(self, multiplier: float) -> ColorProfile:
        """
        Lighten the color profile by a multiplier

        :param multiplier: Multiplier
        :return: Lightened color profile (original isn't modified)
        """
        return ColorProfile([c.lighten(multiplier) for c in self.colors])

    def set_light_raw(self, light: float, at_least: bool | None = None, at_most: bool | None = None) -> 'ColorProfile':
        """
        Set HSL lightness value

        :param light: Lightness value (0-1)
        :param at_least: Set the lightness to at least this value (no change if greater)
        :param at_most: Set the lightness to at most this value (no change if lesser)
        :return: New color profile (original isn't modified)
        """
        return ColorProfile([c.set_light(light, at_least, at_most) for c in self.colors])

    def set_light_dl(self, light: float, term: LightDark = GLOBAL_CFG.light_dark()):
        """
        Set HSL lightness value with respect to dark/light terminals

        :param light: Lightness value (0-1)
        :param term: Terminal color (can be "dark" or "light")
        :return: New color profile (original isn't modified)
        """
        assert term.lower() in ['light', 'dark']
        at_least, at_most = (True, None) if term.lower() == 'dark' else (None, True)
        return self.set_light_raw(light, at_least, at_most)

    def set_light_dl_def(self, term: LightDark | None = None):
        """
        Set default lightness with respect to dark/light terminals

        :param term: Terminal color (can be "dark" or "light")
        :return: New color profile (original isn't modified)
        """
        return self.set_light_dl(GLOBAL_CFG.default_lightness(term), term)

    def unique_colors(self) -> ColorProfile:
        """
        Create another color profile with only the unique colors
        """
        return ColorProfile(remove_duplicates(self.colors))


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

    # below sourced from https://www.flagcolorcodes.com/flags/pride
    # goto f"https://www.flagcolorcodes.com/{preset}" for info
    # todo: sane sorting
    'autosexual': ColorProfile([
        '#99D9EA',
        '#7F7F7F'
    ]),

    'intergender': ColorProfile([
        # todo: use weighted spacing
        '#900DC2',
        '#900DC2',
        '#FFE54F',
        '#900DC2',
        '#900DC2',
    ]),

    'greygender': ColorProfile([
        '#B3B3B3',
        '#B3B3B3',
        '#FFFFFF',
        '#062383',
        '#062383',
        '#FFFFFF',
        '#535353',
        '#535353',
    ]),

    'akiosexual': ColorProfile([
        '#F9485E',
        '#FEA06A',
        '#FEF44C',
        '#FFFFFF',
        '#000000',
    ]),

    'transmasculine': ColorProfile([
        '#FF8ABD',
        '#CDF5FE',
        '#9AEBFF',
        '#74DFFF',
        '#9AEBFF',
        '#CDF5FE',
        '#FF8ABD',
    ]),

    'demifaun': ColorProfile([
        '#7F7F7F',
        '#7F7F7F',
        '#C6C6C6',
        '#C6C6C6',
        '#FCC688',
        '#FFF19C',
        '#FFFFFF',
        '#8DE0D5',
        '#9682EC',
        '#C6C6C6',
        '#C6C6C6',
        '#7F7F7F',
        '#7F7F7F',
    ]),

    'neutrois': ColorProfile([
        '#FFFFFF',
        '#1F9F00',
        '#000000'
    ]),

    'biromantic1': ColorProfile([
        '#8869A5',
        '#D8A7D8',
        '#FFFFFF',
        '#FDB18D',
        '#151638',
    ]),

    'biromantic2': ColorProfile([
        '#740194',
        '#AEB1AA',
        '#FFFFFF',
        '#AEB1AA',
        '#740194',
    ]),

    'autoromantic': ColorProfile([ # symbol interpreted
        '#99D9EA',
        '#99D9EA',
        '#99D9EA',
        '#99D9EA',
        '#99D9EA',
        '#000000',
        '#3DA542',
        '#3DA542',
        '#000000',
        '#7F7F7F',
        '#7F7F7F',
        '#7F7F7F',
        '#7F7F7F',
        '#7F7F7F',
    ]),

    # i didn't expect this one to work. cool!
    'boyflux2': ColorProfile([
        '#E48AE4',
        '#9A81B4',
        '#55BFAB',
        '#FFFFFF',
        '#A8A8A8',
        '#81D5EF',
        '#81D5EF',
        '#81D5EF',
        '#81D5EF',
        '#81D5EF',
        '#69ABE5',
        '#69ABE5',
        '#69ABE5',
        '#69ABE5',
        '#69ABE5',
        '#69ABE5',
        '#69ABE5',
        '#69ABE5',
        '#69ABE5',
        '#69ABE5',
        '#5276D4',
        '#5276D4',
        '#5276D4',
        '#5276D4',
        '#5276D4',
        '#5276D4',
        '#5276D4',
        '#5276D4',
        '#5276D4',
        '#5276D4',
    ]),

    'beiyang': ColorProfile([
        '#DF1B12',
        '#FFC600',
        '#01639D',
        '#FFFFFF',
        '#000000',
    ]),
}
