from __future__ import annotations

import sys
import time
from dataclasses import dataclass
from pathlib import Path
from urllib.request import urlretrieve

from hyfetch.color_util import printc, color
from hyfetch.neofetch_util import term_size


@dataclass
class Theme:
    done_char: str
    todo_char: str
    prefix: str = ''
    suffix: str = ''
    done_len: int = 1
    todo_len: int = 1


CLASSIC_THEME = Theme('█', '.', '[', ']')
NEW_THEME = Theme('&a━', '&c━')
EMOJI_THEME = Theme('✅', '🕑', done_len=2, todo_len=2)
EGG_THEME = Theme('🐣', '🥚', done_len=2, todo_len=2)
FLOWER_THEME = Theme('🌸', '🥀', done_len=2, todo_len=2)


def print_progressbar(total: int, i: int, length: int | None = None, theme: Theme = EMOJI_THEME, unit=''):
    if not length:
        length = term_size()[0]
    i += 1

    completed = f'{i * 100 / total:.0f}%'
    placeholder = 'PLACEHOLDER_BAR'
    template = f'{theme.prefix}{placeholder}{theme.suffix}&r {completed} {i}/{total}{unit}'

    length -= len(template) - len(placeholder) + 2

    progress = int(i / total * length)
    bar = f'{theme.done_char * (progress // theme.todo_len)}{theme.todo_char * ((length - progress) // theme.done_len)}'
    print(color(template.replace(placeholder, bar)), end='\r', flush=True)


def download_pbar(url: str, path: Path):
    def hook(b: int, bsize: int, tsize: int):
        print_progressbar(tsize // 1024 // 1024, b * bsize // 1024 // 1024, unit=' MB')

    if path.is_dir():
        filename = url.split('/')[-1]
        path = path / filename
    path.parent.mkdir(exist_ok=True, parents=True)

    urlretrieve(url, filename=path, reporthook=hook)
    print()


if __name__ == '__main__':
    # theme = {'emoji': EMOJI_THEME, 'flower': FLOWER_THEME, 'egg': EGG_THEME, 'classic': CLASSIC_THEME, 'new': NEW_THEME}
    #
    # for name, t in theme.items():
    #     print(f'\n{name} theme:')
    #     for i in range(100):
    #         print_progressbar(100, i, theme=t)
    #         time.sleep(0.015)
    #     print()
    download_pbar('https://github.com/git-for-windows/git/releases/download/v2.37.2.windows.2/MinGit-2.37.2.2-busybox-64-bit.zip', Path('Downloads'))
