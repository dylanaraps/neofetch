from __future__ import annotations

import os
import re
from pathlib import Path
from subprocess import check_output
from tempfile import TemporaryDirectory

import pkg_resources

from .color_util import AnsiMode
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


def run_neofetch(preset: ColorProfile, mode: AnsiMode):
    # Get existing ascii
    asc = get_distro_ascii()

    # Remove existing colors
    asc = re.sub('\\${.*?}', '', asc)

    # Add new colors
    lines = asc.split('\n')
    colors = preset.with_length(len(lines))
    asc = '\n'.join([colors[i].to_ansi(mode) + l for i, l in enumerate(lines)])

    # Write temp file
    with TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        path = tmp_dir / 'ascii.txt'
        path.write_text(asc)

        # Call neofetch with the temp file
        os.environ['ascii_len'] = str(max(len(l) for l in lines))
        os.environ['ascii_lines'] = str(len(lines))
        os.system(get_command_path() + f' --ascii --source {path.absolute()} --ascii-colors')
