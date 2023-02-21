#!/usr/bin/env python3
"""
This script turns readme shorthand pull request references (i.e. dylanaraps/neofetch#1946) into full
GitHub pull request links.
"""
import regex as re
from pathlib import Path


RE_SHORTHAND = re.compile(r"(\w+?)/(\w+?)#(\d+)")
MY_RE = re.compile(r"(?<=[^\w\[])#(\d+)")


def reformat_readme():
    readme = Path('README.md').read_text()

    readme = re.sub(RE_SHORTHAND, r'[\1#\3](https://github.com/\1/\2/pull/\3)', readme)
    readme = re.sub(MY_RE, r'[#\1](https://github.com/hykilpikonna/hyfetch/pull/\1)', readme)

    Path('README.md').write_text(readme)


if __name__ == '__main__':
    reformat_readme()
