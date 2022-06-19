from __future__ import annotations

import os
import platform
import re
import subprocess
from pathlib import Path
from subprocess import check_output
from tempfile import TemporaryDirectory

import pkg_resources

from .color_util import AnsiMode
from .constants import COLOR_MODE
from .presets import ColorProfile


def get_command_path() -> str:
    """
    Get the absolute path of the neofetch command

    :return: Command path
    """
    return pkg_resources.resource_filename(__name__, 'scripts/neofetch_mod.sh')


def get_distro_ascii() -> str:
    """
    Get the distro ascii

    :return: Distro ascii
    """
    return check_output([get_command_path(), "print_ascii"]).decode().strip()


def get_custom_distro_ascii(distro: str) -> str:
    """
    Get the distro ascii of a specific distro

    :return: Distro ascii
    """
    os.environ['CUSTOM_DISTRO'] = distro
    return check_output([get_command_path(), "print_custom_ascii"]).decode().strip()


def replace_colors(asc: str, preset: ColorProfile, mode: AnsiMode = COLOR_MODE):
    # Remove existing colors
    asc = re.sub('\\${.*?}', '', asc)

    # Add new colors
    lines = asc.split('\n')
    colors = preset.with_length(len(lines))
    asc = '\n'.join([colors[i].to_ansi(mode) + l for i, l in enumerate(lines)])

    return asc, lines


def run_neofetch(preset: ColorProfile, mode: AnsiMode):
    asc, lines = replace_colors(get_distro_ascii(), preset, mode)

    # Write temp file
    with TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        path = tmp_dir / 'ascii.txt'
        path.write_text(asc)

        # Call neofetch with the temp file
        os.environ['ascii_len'] = str(max(len(l) for l in lines))
        os.environ['ascii_lines'] = str(len(lines))

        if platform.system() != 'Windows':
            os.system(f'{get_command_path()} --ascii --source {path.absolute()} --ascii-colors')

        if platform.system() == 'Windows':
            cmd = get_command_path().replace("\\", "/").replace("C:/", "/c/")
            path_str = str(path.absolute()).replace('\\', '/').replace('C:/', '/c/')

            cmd = f'ascii_len={max(len(l) for l in lines)} ascii_lines={len(lines)} ' \
                  f'{cmd} --ascii --source {path_str} --ascii-colors'
            full_cmd = ['C:\\Program Files\\Git\\bin\\bash.exe', '-c', cmd]
            # print(full_cmd)

            subprocess.run(full_cmd)
