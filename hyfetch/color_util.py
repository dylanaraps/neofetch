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

    def to_ansi_256(self, foreground: bool = True) -> str:
        """
        Convert RGB to ANSI 256 Color Escape Code.

        This encoding supports 256 colors in total.

        :return: ANSI 256 escape code like \033[38;5;206m'
        """
        raise NotImplementedError()

    def to_ansi_16(self) -> str:
        """
        Convert RGB to ANSI 16 Color Escape Code

        :return: ANSI 16 escape code
        """
        raise NotImplementedError()
