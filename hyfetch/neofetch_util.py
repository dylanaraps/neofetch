from __future__ import annotations

import os
import platform
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path
from subprocess import check_output
from tempfile import TemporaryDirectory

import pkg_resources
from hyfetch.color_util import color
from typing_extensions import Literal

from .presets import ColorProfile


RE_NEOFETCH_COLOR = re.compile('\\${c[0-9]}')


def ascii_size(asc: str) -> tuple[int, int]:
    """
    Get distro ascii width, height ignoring color code

    :param asc: Distro ascii
    :return: Width, Height
    """
    return max(len(line) for line in re.sub(RE_NEOFETCH_COLOR, '', asc).split('\n')), len(asc.split('\n'))


def normalize_ascii(asc: str) -> str:
    """
    Make sure every line are the same width
    """
    w = ascii_size(asc)[0]
    return '\n'.join(line + ' ' * (w - ascii_size(line)[0]) for line in asc.split('\n'))


@dataclass
class ColorAlignment:
    mode: Literal['horizontal', 'vertical', 'custom']

    # custom_colors[ascii color index] = unique color index in preset
    custom_colors: dict[int, int] = ()

    def recolor_ascii(self, asc: str, preset: ColorProfile) -> str:
        """
        Use the color alignment to recolor an ascii art

        :return Colored ascii, Uncolored lines
        """
        if self.mode in ['horizontal', 'vertical']:
            # Remove existing colors
            asc = re.sub(RE_NEOFETCH_COLOR, '', asc)
            lines = asc.split('\n')

            # Add new colors
            if self.mode == 'horizontal':
                colors = preset.with_length(len(lines))
                asc = '\n'.join([colors[i].to_ansi() + l + color('&r') for i, l in enumerate(lines)])
            else:
                asc = '\n'.join(preset.color_text(line) + color('&r') for line in lines)

        else:
            preset = preset.unique_colors()

            # Apply colors
            new = []
            start_color = None
            color_map = {ai: preset.colors[pi].to_ansi() for ai, pi in self.custom_colors.items()}
            for line in asc.split('\n'):
                # Line has color placeholders
                if len(RE_NEOFETCH_COLOR.findall(line)) > 0:
                    # Get the last placeholder for the next line
                    last = int(RE_NEOFETCH_COLOR.findall(line)[-1][3])

                    # Replace placeholders
                    for ascii_i, c in color_map.items():
                        line = line.replace(f'${{c{ascii_i}}}', c)

                    # Add to new ascii
                    new.append(f'{start_color or ""}{line}')

                    # Change next start color
                    start_color = color_map[last]
                else:
                    new.append(f'{start_color or ""}{line}')

            asc = '\n'.join(new)

        return asc


def get_command_path() -> str:
    """
    Get the absolute path of the neofetch command

    :return: Command path
    """
    return pkg_resources.resource_filename(__name__, 'scripts/neofetch_mod.sh')


def get_distro_ascii(distro: str | None = None) -> str:
    """
    Get the distro ascii of the current distro. Or if distro is specified, get the specific distro's
    ascii art instead.

    :return: Distro ascii
    """
    cmd = 'print_ascii'
    if distro:
        os.environ['CUSTOM_DISTRO'] = distro
        cmd = 'print_custom_ascii'

    return normalize_ascii(check_output([get_command_path(), cmd]).decode().strip())


def run_neofetch(preset: ColorProfile, alignment: ColorAlignment):
    asc = get_distro_ascii()
    w, h = ascii_size(asc)
    asc = alignment.recolor_ascii(asc, preset)

    # Write temp file
    with TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        path = tmp_dir / 'ascii.txt'
        path.write_text(asc)

        # Call neofetch with the temp file
        os.environ['ascii_len'] = str(w)
        os.environ['ascii_lines'] = str(h)

        if platform.system() != 'Windows':
            os.system(f'{get_command_path()} --ascii --source {path.absolute()} --ascii-colors')

        if platform.system() == 'Windows':
            cmd = get_command_path().replace("\\", "/").replace("C:/", "/c/")
            path_str = str(path.absolute()).replace('\\', '/').replace('C:/', '/c/')

            cmd = f'ascii_len={w} ascii_lines={h} {cmd} --ascii --source {path_str} --ascii-colors'
            full_cmd = ['C:\\Program Files\\Git\\bin\\bash.exe', '-c', cmd]
            # print(full_cmd)

            subprocess.run(full_cmd)
