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

    def with_weights(self, weights: list[int]) -> list[RGB]:
        """
        Map colors based on weights

        :param weights: Weights of each color (weights[i] = how many times color[i] appears)
        :return:
        """
        colors = self.decode()
        return [c for i, w in enumerate(weights) for c in [colors[i]] * w]

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
            weights[-border_i] += 1
            border_i += 1

        return self.with_weights(weights)
