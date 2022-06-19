#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from typing_extensions import Literal

from . import constants
from .color_util import AnsiMode, printc, color, clear_screen, RGB
from .constants import CONFIG_PATH, VERSION, TERM_LEN, TEST_ASCII_WIDTH
from .neofetch_util import run_neofetch, replace_colors, get_custom_distro_ascii
from .presets import PRESETS, ColorProfile
from .serializer import json_stringify


@dataclass
class Config:
    preset: str
    mode: AnsiMode
    light_dark: Literal['light', 'dark'] = 'dark'

    def save(self):
        CONFIG_PATH.parent.mkdir(exist_ok=True, parents=True)
        CONFIG_PATH.write_text(json_stringify(self), 'utf-8')


def check_config() -> Config:
    """
    Check if the configuration exists. Return the config object if it exists. If not, call the
    config creator

    TODO: Config path param

    :return: Config object
    """
    if CONFIG_PATH.is_file():
        return Config(**json.loads(CONFIG_PATH.read_text('utf-8')))

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
    constants.COLOR_MODE = color_system
    title += f'\n&e1. Selected color mode: &r{color_system}'

    ##############################
    # 2. Choose preset
    clear_screen(title)
    printc('&a2. Let\'s choose a flag!')
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
        for line in zip(*current):
            printc('  '.join(line))

        print()

    print()
    tmp = PRESETS['rainbow'].set_light(.7).color_text('preset')
    preset = literal_input(f'Which {tmp} do you want to use?', PRESETS.keys(), 'rainbow', show_ops=False)
    title += f'\n&e2. Selected flag:       &r{PRESETS[preset].color_text(preset)}'

    ##############################
    # 3. Select light/dark mode
    clear_screen(title)
    light_dark = literal_input(f'3. Is your terminal in &gf(#85e7e9)light mode&r or &gf(#c471ed)dark mode&r?',
                               ['light', 'dark'], 'dark')
    is_light = light_dark == 'light'
    title += f'\n&e3. Light/Dark:          &r{light_dark}'

    # Create config
    c = Config(preset, color_system, light_dark)

    # Save config
    save = literal_input(f'Save config?', ['y', 'n'], 'y')
    if save == 'y':
        c.save()

    return c


def run():
    # Create CLI
    hyfetch = color('&b&lhy&f&lfetch&r')
    parser = argparse.ArgumentParser(description=color(f'{hyfetch} - neofetch with flags <3'))

    parser.add_argument('-c', '--config', action='store_true', help=color(f'Configure {hyfetch}'))
    parser.add_argument('-p', '--preset', help=f'Use preset', choices=PRESETS.keys())
    parser.add_argument('-m', '--mode', help=f'Color mode', choices=['8bit', 'rgb'])
    parser.add_argument('--c-scale', dest='scale', help=f'Lighten colors by a multiplier', type=float)
    parser.add_argument('--c-set-l', dest='light', help=f'Set lightness value of the colors', type=float)
    parser.add_argument('-V', '--version', dest='version', action='store_true', help=f'Check version')
    parser.add_argument('--debug', action='store_true', help=color(f'Debug mode'))
    parser.add_argument('--test-distro', help=color(f'Test print a specific distro\'s ascii art'))

    args = parser.parse_args()

    if args.version:
        print(f'Version is {VERSION}')
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
    constants.COLOR_MODE = config.mode

    # Get preset
    preset = PRESETS.get(config.preset)

    # Lighten
    if args.scale:
        preset = preset.lighten(args.scale)
    if args.light:
        preset = preset.set_light(args.light)

    # Test distro ascii art
    if args.test_distro:
        asc = get_custom_distro_ascii(args.test_distro)
        print(asc)
        print(replace_colors(asc, preset, config.mode)[0])
        return

    # Run
    run_neofetch(preset, config.mode)
