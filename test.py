from hyfetch.color_util import RGB
from hyfetch.presets import PRESETS


def print_colors_test(colors: list[RGB]):
    print(''.join(f'{c.to_ansi_rgb()}#' for c in colors))


if __name__ == '__main__':
    p = PRESETS.get('transgender')
    print_colors_test(p.with_length(9))
    print_colors_test(p.with_length(6))
    p = PRESETS.get('nonbinary')
    print_colors_test(p.with_length(7))
    print_colors_test(p.with_length(6))
