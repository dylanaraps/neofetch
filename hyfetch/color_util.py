from typing import NamedTuple


class RGB(NamedTuple):
    r: int
    g: int
    b: int

    @classmethod
    def from_hex(cls, hex: str) -> "RGB":
        """
        Create color from hex code

        >>> RGB.from_hex('#FFAAB7')
        RGB(r=255, g=170, b=183)

        :param hex: Hex color code
        :return: RGB object
        """
        while hex.startswith('#'):
            hex = hex[1:]

        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)
        return cls(r, g, b)
