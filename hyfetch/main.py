#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import random
import re
from itertools import permutations
from typing import Iterable

from hyfetch import presets

from .color_util import printc, color, clear_screen, LightDark
from .constants import CONFIG_PATH, VERSION, TERM_LEN, TEST_ASCII_WIDTH, TEST_ASCII, GLOBAL_CFG
from .models import Config
from .neofetch_util import run_neofetch, get_distro_ascii, ColorAlignment, ascii_size, color_alignments
from .presets import PRESETS


def check_config() -> Config:
    """
    Check if the configuration exists. Return the config object if it exists. If not, call the
    config creator

    TODO: Config path param

    :return: Config object
    """
    if CONFIG_PATH.is_file():
        try:
            return Config.from_dict(json.loads(CONFIG_PATH.read_text('utf-8')))
        except KeyError:
            return create_config()

    return create_config()


def literal_input(prompt: str, options: Iterable[str], default: str, show_ops: bool = True) -> str:
    """
    Ask the user to provide an input among a list of options

    :param prompt: Input prompt
    :param options: Options
    :param default: Default option
    :param show_ops: Show options
    :return: Selection
    """
    options = list(options)
    lows = [o.lower() for o in options]

    if show_ops:
        op_text = '|'.join([f'&l&n{o}&r' if o == default else o for o in options])
        printc(f'{prompt} ({op_text})')
    else:
        printc(f'{prompt} (default: {default})')

    selection = input('> ') or default
    while not selection.lower() in lows:
        print(f'Invalid selection! {selection} is not one of {"|".join(options)}')
        selection = input('> ') or default
    print()

    return options[lows.index(selection)]


def create_config() -> Config:
    """
    Create config interactively

    :return: Config object (automatically stored)
    """
    title = 'Welcome to &b&lhy&f&lfetch&r! Let\'s set up some colors first.'
    clear_screen(title)

    ##############################
    # 1. Select color system
    try:
        # Demonstrate RGB with a gradient. This requires numpy
        from .color_scale import Scale

        scale2 = Scale(['#12c2e9', '#c471ed', '#f7797d'])
        _8bit = [scale2(i / TERM_LEN).to_ansi_8bit(False) for i in range(TERM_LEN)]
        _rgb = [scale2(i / TERM_LEN).to_ansi_rgb(False) for i in range(TERM_LEN)]

        printc('&f' + ''.join(c + t for c, t in zip(_8bit, '8bit Color Testing'.center(TERM_LEN))))
        printc('&f' + ''.join(c + t for c, t in zip(_rgb, 'RGB Color Testing'.center(TERM_LEN))))

        print()
        printc(f'&a1. Which &bcolor system &ado you want to use?')
        printc(f'(If you can\'t see colors under "RGB Color Testing", please choose 8bit)')
        print()
        color_system = literal_input('Your choice?', ['8bit', 'rgb'], 'rgb')

    except ModuleNotFoundError:
        # Numpy not found, skip gradient test, use fallback
        color_system = literal_input('Which &acolor &bsystem &rdo you want to use?',
                                     ['8bit', 'rgb'], 'rgb')

    # Override global color mode
    GLOBAL_CFG.color_mode = color_system
    title += f'\n&e1. Selected color mode: &r{color_system}'

    ##############################
    # 2. Select light/dark mode
    clear_screen(title)
    light_dark = literal_input(f'2. Is your terminal in &gf(#85e7e9)light mode&r or &gf(#c471ed)dark mode&r?',
                               ['light', 'dark'], 'dark')
    is_light = light_dark == 'light'
    GLOBAL_CFG.is_light = is_light
    title += f'\n&e2. Light/Dark:          &r{light_dark}'

    ##############################
    # 3. Choose preset
    clear_screen(title)
    printc('&a3. Let\'s choose a flag!')
    printc('Available flag presets:')
    print()

    # Create flags = [[lines]]
    flags = []
    spacing = max(max(len(k) for k in PRESETS.keys()), 20)
    for name, preset in PRESETS.items():
        flag = preset.color_text(' ' * spacing, foreground=False)
        flags.append([name.center(spacing), flag, flag, flag])

    # Calculate flags per row
    flags_per_row = TERM_LEN // (spacing + 2)
    while flags:
        current = flags[:flags_per_row]
        flags = flags[flags_per_row:]

        # Print by row
        [printc('  '.join(line)) for line in zip(*current)]
        print()

    print()
    tmp = PRESETS['rainbow'].set_light_dl_def(light_dark).color_text('preset')
    preset = literal_input(f'Which {tmp} do you want to use?', PRESETS.keys(), 'rainbow', show_ops=False)
    _prs = PRESETS[preset]
    title += f'\n&e3. Selected flag:       &r{_prs.color_text(preset)}'

    #############################
    # 4. Dim/lighten colors
    clear_screen(title)
    printc(f'&a4. Let\'s adjust the color brightness!')
    printc(f'The colors might be a little bit too {"bright" if is_light else "dark"} for {light_dark} mode.')
    print()

    # Print cats
    num_cols = TERM_LEN // (TEST_ASCII_WIDTH + 2)
    ratios = [col / (num_cols - 1) for col in range(num_cols)]
    ratios = [(r * 0.4 + 0.1) if is_light else (r * 0.4 + 0.5) for r in ratios]
    lines = [ColorAlignment('horizontal').recolor_ascii(TEST_ASCII.replace(
        '{txt}', f'{r * 100:.0f}%'.center(5)), _prs.set_light_dl(r, light_dark)).split('\n') for r in ratios]
    [printc('  '.join(line)) for line in zip(*lines)]

    while True:
        print()
        printc(f'Which brightness level look the best? (Default: left blank = {GLOBAL_CFG.default_lightness(light_dark):.2f} for {light_dark} mode)')
        lightness = input('> ').strip().lower() or None

        # Parse lightness
        if not lightness or lightness in ['unset', 'none']:
            lightness = None
            break

        try:
            lightness = int(lightness[:-1]) / 100 if lightness.endswith('%') else float(lightness)
            assert 0 <= lightness <= 1
            break

        except Exception:
            printc('&cUnable to parse lightness value, please input it as a decimal or percentage (e.g. 0.5 or 50%)')

    if lightness:
        _prs = _prs.set_light_dl(lightness, light_dark)
    title += f'\n&e4. Brightness:          &r{f"{lightness:.2f}" if lightness else "unset"}'

    #############################
    # 5. Color arrangement
    color_alignment = None
    while True:
        clear_screen(title)
        printc(f'&a5. Let\'s choose a color arrangement!')
        printc(f'You can choose standard horizontal or vertical alignment, or use one of the random color schemes, or assign colors yourself (TODO).')
        print()

        asc = get_distro_ascii()
        asc_width = ascii_size(asc)[0]
        asciis = [
            [*ColorAlignment('horizontal').recolor_ascii(asc, _prs).split('\n'), 'Horizontal'.center(asc_width)],
            [*ColorAlignment('vertical').recolor_ascii(asc, _prs).split('\n'), 'Vertical'.center(asc_width)],
        ]
        ascii_per_row = TERM_LEN // (asc_width + 2)

        # Random color schemes
        # ascii_indices =
        pis = list(range(len(_prs.unique_colors().colors)))
        while len(pis) < len(set(re.findall('(?<=\\${c)[0-9](?=})', asc))):
            pis += pis
        perm = list(permutations(pis))
        random_count = ascii_per_row * 2 - 2
        choices = random.sample(perm, random_count)
        choices = [{i: n for i, n in enumerate(c)} for c in choices]
        asciis += [[*ColorAlignment('custom', r).recolor_ascii(asc, _prs).split('\n'), f'random{i}'.center(asc_width)]
                   for i, r in enumerate(choices)]

        while asciis:
            current = asciis[:ascii_per_row]
            asciis = asciis[ascii_per_row:]

            # Print by row
            [printc('  '.join(line)) for line in zip(*current)]
            print()

        print('You can type "roll" to randomize again.')
        print()
        choice = literal_input(f'Your choice?', ['horizontal', 'vertical', 'roll'] + [f'random{i}' for i in range(random_count)], 'horizontal')

        if choice == 'roll':
            continue

        if choice in ['horizontal', 'vertical']:
            color_alignment = ColorAlignment(choice)
        elif choice.startswith('random'):
            color_alignment = ColorAlignment('custom', choices[int(choice[6])])
        else:
            raise NotImplementedError()

        break

    title += f'\n&e5. Color Alignment:     &r{color_alignment}'

    # Create config
    clear_screen(title)
    c = Config(preset, color_system, light_dark, lightness, color_alignment)

    # Save config
    print()
    save = literal_input(f'Save config?', ['y', 'n'], 'y')
    if save == 'y':
        c.save()

    return c


def run():
    # Create CLI
    hyfetch = color('&b&lhyfetch&r')
    parser = argparse.ArgumentParser(description=color(f'{hyfetch} - neofetch with flags <3'))

    parser.add_argument('-c', '--config', action='store_true', help=color(f'Configure {hyfetch}'))
    parser.add_argument('-p', '--preset', help=f'Use preset', choices=PRESETS.keys())
    parser.add_argument('-m', '--mode', help=f'Color mode', choices=['8bit', 'rgb'])
    parser.add_argument('--c-scale', dest='scale', help=f'Lighten colors by a multiplier', type=float)
    parser.add_argument('--c-set-l', dest='light', help=f'Set lightness value of the colors', type=float)
    parser.add_argument('-V', '--version', dest='version', action='store_true', help=f'Check version')
    parser.add_argument('--debug', action='store_true', help=color(f'Debug mode'))
    parser.add_argument('--debug-list', help=color(f'Debug recommendations'))
    parser.add_argument('--test-distro', help=color(f'Test for a specific distro'))
    parser.add_argument('--test-print', action='store_true', help=color(f'Test print distro ascii art only'))

    args = parser.parse_args()

    if args.version:
        print(f'Version is {VERSION}')
        return

    # Test distro ascii art
    if args.test_distro:
        print(f'Setting distro to {args.test_distro}')
        GLOBAL_CFG.override_distro = args.test_distro

    if args.debug:
        GLOBAL_CFG.debug = True

    if args.test_print:
        print(get_distro_ascii())
        return

    # Load config
    config = check_config()

    # Reset config
    if args.config:
        config = create_config()

    # Param overwrite config
    if args.preset:
        config.preset = args.preset
    if args.mode:
        config.mode = args.mode

    # Override global color mode
    GLOBAL_CFG.color_mode = config.mode
    GLOBAL_CFG.is_light = config.light_dark == 'light'

    # Get preset
    preset = PRESETS.get(config.preset)

    # Lighten
    if args.scale:
        preset = preset.lighten(args.scale)
    if args.light:
        preset = preset.set_light_raw(args.light)
    if config.lightness:
        preset = preset.set_light_dl(config.lightness)

    # Debug recommendations
    if args.debug_list:
        distro = args.debug_list
        ca = color_alignments[distro]

        print(distro)
        GLOBAL_CFG.override_distro = distro
        asciis = [ca.recolor_ascii(get_distro_ascii(distro), p).split('\n') for p in list(PRESETS.values())[:3]]
        [printc('  '.join(line)) for line in zip(*asciis)]
        return

    # Run
    run_neofetch(preset, config.color_align)
