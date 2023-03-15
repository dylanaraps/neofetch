from hyfetch.color_scale import test_color_scale
from hyfetch.color_util import RGB, printc
from hyfetch.neofetch_util import get_command_path
from hyfetch.presets import PRESETS


def print_colors_test(colors: list[RGB]):
    print(''.join(f'{c.to_ansi_rgb()}#' for c in colors))


def test_preset_length():
    p = PRESETS.get('transgender')
    print_colors_test(p.with_length(9))
    print_colors_test(p.with_length(6))
    p = PRESETS.get('nonbinary')
    print_colors_test(p.with_length(7))
    print_colors_test(p.with_length(6))


def test_command_path():
    print(get_command_path())


def test_rgb_8bit_conversion():
    for r in range(0, 255, 16):
        for g in range(0, 255, 16):
            print(RGB(r, g, 0).to_ansi_rgb(False), end=' ')
        printc('&*')
    print()
    for r in range(0, 255, 16):
        for g in range(0, 255, 16):
            print(RGB(r, g, 0).to_ansi_8bit(False), end=' ')
        printc('&*')
    print()


if __name__ == '__main__':
    test_rgb_8bit_conversion()
    test_color_scale()
