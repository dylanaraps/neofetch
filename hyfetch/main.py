#!/usr/bin/env python3

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Iterable

from hypy_utils import printc, json_stringify

from .presets import PRESETS


CONFIG_PATH = Path.home() / '.config/hyfetch.json'
CONFIG_PATH.parent.mkdir(exist_ok=True, parents=True)


@dataclass
class Config:
    preset: str
    mode: Literal['default', 'ansi', '8bit', 'rgb']

    def save(self):
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


def center_text(txt: str, spaces: int) -> str:
    """
    Put the text in the center in a defined space

    >>> center_text('meow', 9)
    '  meow   '

    :param txt: Text
    :param spaces: Total space of the text
    :return: Text with length spaces
    """
    spaces -= len(txt)

    if spaces % 2 == 1:
        spaces -= 1
        txt += ' '

    while spaces > 0:
        spaces -= 2
        txt = f' {txt} '

    return txt


def create_config() -> Config:
    """
    Create config interactively

    :return: Config object (automatically stored)
    """
    # Select color system
    # TODO: Demo of each color system
    color_system = literal_input('Which &acolor &bsystem &rdo you want to use?',
                                 ['ansi', '8bit', 'rgb'], 'rgb')

    # Print preset
    print('Available presets:')
    spacing = max(max(len(k) for k in PRESETS.keys()), 30)
    for name, preset in PRESETS.items():
        printc(preset.color_text(center_text(name, spacing), foreground=False))

        # preset_demo = ''.join(f'{c.to_ansi_rgb(False)} ' for c in preset.with_length(flag_length))
        # printc(name + ' ' * (spacing - len(name)) + preset_demo)

    print()
    tmp = PRESETS['rainbow'].color_text('preset')
    preset = literal_input(f'Which {tmp} do you want to use?', PRESETS.keys(), 'rainbow')

    # Save and return
    c = Config(preset, color_system)
    c.save()
    return c


def run():
    parser = argparse.ArgumentParser(description='neofetch with flags <3')
    config = check_config()
    # TODO: --setup command
