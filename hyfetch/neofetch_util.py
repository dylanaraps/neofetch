from __future__ import annotations

import inspect
import os
import platform
import re
import shlex
import subprocess
import sys
import zipfile
from dataclasses import dataclass
from pathlib import Path
from subprocess import check_output
from tempfile import TemporaryDirectory
from urllib.request import urlretrieve

import pkg_resources
from typing_extensions import Literal

from hyfetch.color_util import color
from .constants import GLOBAL_CFG, MINGIT_URL
from .presets import ColorProfile
from .serializer import from_dict

RE_NEOFETCH_COLOR = re.compile('\\${c[0-9]}')


def term_size() -> tuple[int, int]:
    """
    Get terminal size
    :return:
    """
    try:
        return os.get_terminal_size().columns, os.get_terminal_size().lines
    except Exception:
        return 100, 20


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


def fill_starting(asc: str) -> str:
    """
    Fill the missing starting placeholders.

    E.g. "${c1}...\n..." -> "${c1}...\n${c1}..."
    """
    new = []
    last = ''
    for line in asc.split('\n'):
        new.append(last + line)

        # Line has color placeholders
        matches = RE_NEOFETCH_COLOR.findall(line)
        if len(matches) > 0:
            # Get the last placeholder for the next line
            last = matches[-1]

    return '\n'.join(new)


@dataclass
class ColorAlignment:
    mode: Literal['horizontal', 'vertical', 'custom']

    # custom_colors[ascii color index] = unique color index in preset
    custom_colors: dict[int, int] = ()

    # Foreground/background ascii color index
    fore_back: tuple[int, int] = ()

    @classmethod
    def from_dict(cls, d: dict):
        return from_dict(cls, d)

    def recolor_ascii(self, asc: str, preset: ColorProfile) -> str:
        """
        Use the color alignment to recolor an ascii art

        :return Colored ascii, Uncolored lines
        """
        asc = fill_starting(asc)

        if self.fore_back and self.mode in ['horizontal', 'vertical']:
            fore, back = self.fore_back

            # Replace foreground colors
            asc = asc.replace(f'${{c{fore}}}', color('&0' if GLOBAL_CFG.is_light else '&f'))
            lines = asc.split('\n')

            # Add new colors
            if self.mode == 'horizontal':
                colors = preset.with_length(len(lines))
                asc = '\n'.join([l.replace(f'${{c{back}}}', colors[i].to_ansi()) + color('&r') for i, l in enumerate(lines)])
            else:
                raise NotImplementedError()

            # Remove existing colors
            asc = re.sub(RE_NEOFETCH_COLOR, '', asc)

        elif self.mode in ['horizontal', 'vertical']:
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
            color_map = {ai: preset.colors[pi].to_ansi() for ai, pi in self.custom_colors.items()}
            for ascii_i, c in color_map.items():
                asc = asc.replace(f'${{c{ascii_i}}}', c)

        return asc


def get_command_path() -> str:
    """
    Get the absolute path of the neofetch command

    :return: Command path
    """
    cmd_path = pkg_resources.resource_filename(__name__, 'scripts/neowofetch')

    # Windows doesn't support symbolic links, but also I can't detect symbolic links... hard-code it here for now.
    if platform.system() == 'Windows':
        return str(Path(cmd_path).parent.parent.parent / 'neofetch')

    return cmd_path


def ensure_git_bash() -> Path:
    """
    Ensure git bash installation for windows

    :returns git bash path
    """
    if platform.system() == 'Windows':
        # Find installation in default path
        def_path = Path(r'C:\Program Files\Git\bin\bash.exe')
        if def_path.is_file():
            return def_path

        # Find installation in PATH (C:\Program Files\Git\cmd should be in path)
        pth = (os.environ.get('PATH') or '').lower().split(';')
        pth = [p for p in pth if p.endswith(r'\git\cmd')]
        if pth:
            return Path(pth[0]).parent / r'bin\bash.exe'

        # Previously downloaded portable installation
        path = Path(__file__).parent / 'min_git'
        pkg_path = path / 'package.zip'
        if path.is_dir():
            return path / r'bin\bash.exe'

        # No installation found, download a portable installation
        print('Git installation not found. Git is required to use HyFetch/neofetch on Windows')
        print('Downloading a minimal portable package for Git...')
        urlretrieve(MINGIT_URL, pkg_path)
        print('Download finished! Extracting...')
        with zipfile.ZipFile(pkg_path, 'r') as zip_ref:
            zip_ref.extractall(path)
        print('Done!')
        return path / r'bin\bash.exe'


def check_windows_cmd():
    """
    Check if this script is running under cmd.exe. If so, launch an external window with git bash
    since cmd doesn't support RGB colors.
    """
    if platform.system() == 'Windows':
        import psutil
        # TODO: This line does not correctly identify cmd prompts...
        if psutil.Process(os.getppid()).name().lower().strip() == 'cmd.exe':
            print("cmd.exe doesn't support RGB colors, restarting in MinTTY...")
            cmd = f'"{ensure_git_bash().parent.parent / "usr/bin/mintty.exe"}" -s 110,40 -e python -m hyfetch --ask-exit'
            os.system(cmd)
            sys.exit(0)


def run_command(args: str, pipe: bool = False) -> str | None:
    """
    Run neofetch command
    """
    if platform.system() != 'Windows':
        full_cmd = shlex.split(f'/usr/bin/env bash {get_command_path()} {args}')

    else:
        cmd = get_command_path().replace("\\", "/").replace("C:/", "/c/")
        args = args.replace('\\', '/').replace('C:/', '/c/')

        full_cmd = [ensure_git_bash(), '-c', f'{cmd} {args}']
    # print(full_cmd)

    if pipe:
        return check_output(full_cmd).decode().strip()
    else:
        subprocess.run(full_cmd)


def get_distro_ascii(distro: str | None = None) -> str:
    """
    Get the distro ascii of the current distro. Or if distro is specified, get the specific distro's
    ascii art instead.

    :return: Distro ascii
    """
    if not distro and GLOBAL_CFG.override_distro:
        distro = GLOBAL_CFG.override_distro
    if GLOBAL_CFG.debug:
        print(distro)
        print(GLOBAL_CFG)
    cmd = 'print_ascii'
    if distro:
        os.environ['CUSTOM_DISTRO'] = distro
        cmd = 'print_custom_ascii'

    asc = run_command(cmd, True)

    # Unescape backslashes here because backslashes are escaped in neofetch for printf
    asc = asc.replace('\\\\', '\\')

    return normalize_ascii(asc)


def get_distro_name():
    return run_command('ascii_distro_name', True)


def run_neofetch(preset: ColorProfile, alignment: ColorAlignment):
    """
    Run neofetch with colors

    :param preset: Color palette
    :param alignment: Color alignment settings
    """
    asc = get_distro_ascii()
    w, h = ascii_size(asc)
    asc = alignment.recolor_ascii(asc, preset)

    # Escape backslashes here because backslashes are escaped in neofetch for printf
    asc = asc.replace('\\', '\\\\')

    # Write temp file
    with TemporaryDirectory() as tmp_dir:
        tmp_dir = Path(tmp_dir)
        path = tmp_dir / 'ascii.txt'
        path.write_text(asc)

        # Call neofetch with the temp file
        os.environ['ascii_len'] = str(w)
        os.environ['ascii_lines'] = str(h)

        run_command(f'--ascii --source {path.absolute()} --ascii-colors')


def get_fore_back(distro: str | None = None) -> tuple[int, int] | None:
    """
    Get recommended foreground-background configuration for distro, or None if the distro ascii is
    not suitable for fore-back configuration.

    :return:
    """
    if not distro and GLOBAL_CFG.override_distro:
        distro = GLOBAL_CFG.override_distro
    if not distro:
        distro = get_distro_name().lower()
    distro = distro.lower().replace(' ', '-')
    for k, v in fore_back.items():
        if distro == k.lower():
            return v
    return None


# Foreground-background recommendation
fore_back = {
    'fedora': (2, 1),
    'ubuntu': (2, 1),
    'kubuntu': (2, 1),
    'lubuntu': (2, 1),
    'xubuntu': (2, 1),
    'ubuntu-cinnamon': (2, 1),
    'ubuntu-kylin': (2, 1),
    'ubuntu-mate': (2, 1),
    'ubuntu-studio': (2, 1),
    'ubuntu-sway': (2, 1),
}

