#!/usr/bin/env python3
"""
This script turns readme shorthand pull request references (i.e. dylanaraps/neofetch#1946) into full
GitHub pull request links.
"""
import re
from pathlib import Path


RE_SHORTHAND = re.compile(r"""[a-z0-9]+?/[a-z0-9]+?#[0-9]+""")


def reformat_readme():
    readme = Path('README.md').read_text()

    for shorthand in RE_SHORTHAND.findall(readme):
        user, pull = shorthand.split('/')
        repo, pull = pull.split('#')
        readme = readme.replace(shorthand, f'[{user}#{pull}](https://github.com/{user}/{repo}/pull/{pull})')

    Path('README.md').write_text(readme)


if __name__ == '__main__':
    reformat_readme()
