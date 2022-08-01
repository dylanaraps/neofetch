"""
List distributions supported by neofetch
"""
from __future__ import annotations

import string
import textwrap
from dataclasses import dataclass

from pathlib import Path

import regex

RE_SPLIT = regex.compile('EOF[ \n]*?;;')
RE_COLORS = regex.compile("""(?<=set_colors )[a-z\\d ]+(?=\n)""")


@dataclass
class AsciiArt:
    match: str
    color: str
    ascii: str

    def get_friendly_name(self) -> str:
        return self.match.split("|")[0].strip(string.punctuation + '* ')\
            .replace('"', '').replace('*', '')


def substr(s: str, start: str, end: str | None = None):
    """
    Get substring between start and end
    """
    start = s.index(start) + len(start)

    if end is None:
        return s[start:]

    return s[start:s.index(end, start)]


def parse_ascii_distros() -> list[AsciiArt]:
    """
    Parse ascii distros from neofetch script
    """
    nf = (Path(__file__).parent.parent / 'neofetch').read_text()

    # Get the content of "get_distro_ascii" function
    nf = nf[nf.index('get_distro_ascii() {\n'):]
    nf = nf[:nf.index('\n}\n')]

    # Remove trailing spaces
    while ' \n' in nf:
        nf = nf.replace(' \n', '\n')

    # Split by blocks
    blocks = [sub.strip() for b in regex.split('case .*? in\n', nf) for sub in RE_SPLIT.split(b)]

    # Parse blocks
    def parse_block(block: str) -> AsciiArt:
        try:
            # Get ascii art
            assert "'EOF'\n" in block
            art = substr(block, "'EOF'\n")

            # Join \
            block = block.replace('\\\n', ' ')

            # Get switch-case matching parameter
            match = block.split('\n')[0].strip()
            assert match.endswith(')')
            match = match[:-1]

            # Get colors
            color = RE_COLORS.findall(block)[0]
            if len(color) == 0:
                raise Exception(block)

            return AsciiArt(match, color, art)

        except AssertionError:
            pass

    out = [parse_block(block) for block in blocks]
    return [v for v in out if v]

