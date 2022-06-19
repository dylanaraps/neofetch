#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from .color_util import AnsiMode, printc, color, clear_screen, RGB
from .neofetch_util import run_neofetch, replace_colors, get_custom_distro_ascii
from .presets import PRESETS, ColorProfile
from .serializer import json_stringify

CONFIG_PATH = Path.home() / '.config/hyfetch.json'
VERSION = '1.0.7'


# Obtain terminal size
try:
    term_len = os.get_terminal_size().columns
except Exception:
    term_len = 40


@dataclass
class Config:
    preset: str
    mode: AnsiMode

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


def literal_input(prompt: str, options: Iterable[str], default: str) -> str:
    """
    Ask the user to provide an input among a list of options

    :param prompt: Input prompt
    :param options: Options
    :param default: Default option
    :return: Selection
    """
    options = list(options)
    lows = [o.lower() for o in options]

    op_text = '|'.join([f'&l&n{o}&r' if o == default else o for o in options])
    printc(f'{prompt} ({op_text})')
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
    title = '\nWelcome to &b&lhy&f&lfetch&r! Let\'s set up some colors first.\n'
    clear_screen(title)

    ##############################
    # 1. Select color system
    try:
        # Demonstrate RGB with a gradient. This requires numpy
        from .color_scale import Scale

        scale2 = Scale(['#12c2e9', '#c471ed', '#f7797d'])
        _8bit = [scale2(i / term_len).to_ansi_8bit(False) for i in range(term_len)]
        _rgb = [scale2(i / term_len).to_ansi_rgb(False) for i in range(term_len)]

        printc('&f' + ''.join(c + t for c, t in zip(_8bit, '8bit Color Testing'.center(term_len))))
        printc('&f' + ''.join(c + t for c, t in zip(_rgb, 'RGB Color Testing'.center(term_len))))

        print()
        printc(f'1. Which &acolor &bsystem &rdo you want to use?')
        printc(f'(If you can\'t see colors under "RGB Color Testing", please choose 8bit)')
        print()
        color_system = literal_input('Your choice?', ['8bit', 'rgb'], 'rgb')

    except ModuleNotFoundError:
        # Numpy not found, skip gradient test, use fallback
        color_system = literal_input('Which &acolor &bsystem &rdo you want to use?',
                                     ['8bit', 'rgb'], 'rgb')
    color_system = AnsiMode(color_system)


    ##############################
    # 3. Choose preset
    clear_screen(title)
    print('2. Let\'s choose a flag! Available flags:\n')

    # Create flags = [[lines]]
    flags = []
    spacing = max(max(len(k) for k in PRESETS.keys()), 20)
    for name, preset in PRESETS.items():
        flag = preset.color_text(' ' * spacing, foreground=False)
        flags.append([name.center(spacing), flag, flag, flag])

    # Calculate flags per row
    flags_per_row = term_len // (spacing + 2)
    while flags:
        current = flags[:flags_per_row]
        flags = flags[flags_per_row:]

        # Print by row
        for line in range(len(current[0])):
            printc('  '.join(flag[line] for flag in current))

        print()

    print()
    tmp = PRESETS['rainbow'].color_text('preset')
    preset = literal_input(f'Which {tmp} do you want to use?', PRESETS.keys(), 'rainbow')

    # Create config
    c = Config(preset, color_system)

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

    preset = PRESETS.get(config.preset)

    # Lighten
    if args.scale:
        preset = ColorProfile([c.lighten(args.scale) for c in preset.colors])
    if args.light:
        preset = ColorProfile([c.set_light(args.light) for c in preset.colors])

    # Test distro ascii art
    if args.test_distro:
        asc = get_custom_distro_ascii(args.test_distro)
        print(asc)
        print(replace_colors(asc, preset, config.mode)[0])
        exit(0)

    # Run
    run_neofetch(preset, config.mode)
