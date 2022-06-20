from __future__ import annotations

import numpy as np
from numpy import ndarray

from .color_util import RGB


def create_gradient_hex(colors: list[str], resolution: int = 300) -> ndarray:
    """
    Create gradient array from hex
    """
    colors = np.array([RGB.from_hex(s) for s in colors])
    return create_gradient(colors, resolution)


def create_gradient(colors: ndarray, resolution: int) -> ndarray:
    """
    Create gradient 2d array.

    Usage: arr[ratio / len(arr), :] = Scaled gradient color at that point
    """
    result = np.zeros((resolution * (len(colors) - 1), 3), dtype='uint8')

    # Create gradient mapping
    for i in range(len(colors) - 1):
        c1 = colors[i, :]
        c2 = colors[i + 1, :]
        bi = i * resolution

        for r in range(resolution):
            ratio = r / resolution
            result[bi + r, :] = c2 * ratio + c1 * (1 - ratio)

    return result


def get_raw(gradient: ndarray, ratio: float) -> ndarray:
    """
    :param gradient: Gradient array (2d)
    :param ratio: Between 0-1
    :return: RGB subarray (1d, has 3 values)
    """
    if ratio == 1:
        return gradient[-1, :]

    i = int(ratio * len(gradient))
    return gradient[i, :]


class Scale:
    colors: ndarray
    rgb: ndarray

    def __init__(self, scale: list[str], resolution: int = 300):
        self.colors = np.array([RGB.from_hex(s) for s in scale])
        self.rgb = create_gradient(self.colors, resolution)

    def __call__(self, ratio: float) -> RGB:
        """
        :param ratio: Between 0-1
        """
        return RGB(*get_raw(self.rgb, ratio))


def test_color_scale():
    scale = Scale(['#232323', '#4F1879', '#B43A78', '#F98766', '#FCFAC0'])

    colors = 100
    for i in range(colors + 1):
        print(scale(i / colors).to_ansi_rgb(False), end=' ')
