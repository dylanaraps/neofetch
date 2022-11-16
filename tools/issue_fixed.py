#!/usr/bin/env python3
import shlex
from subprocess import check_output

import pyperclip


def copy_comment():
    # Get commit SHA
    sha = check_output(shlex.split('git rev-parse --short HEAD')).decode().strip()

    # Copy comment to clipboard
    comment = f"""
Thank you for reporting the issue!

This issue is [fixed in hyfetch by commit {sha}](https://github.com/hykilpikonna/hyfetch/commit/{sha}). This repo (dylanaraps/neofetch) seems to be no longer maintained.

[HyFetch](https://github.com/hykilpikonna/hyfetch) is a fork of neofetch with LGBTQ pride flags, but the repo also maintains an updated version of the original neofetch, addressing many issues and pull requests.

Read the ["Running Updated Original Neofetch" section](https://github.com/hykilpikonna/hyfetch#running-updated-original-neofetch) for more info!
    """
    pyperclip.copy(comment.strip())
    print()
    print('Comment response copied to clipboard.')


if __name__ == '__main__':
    copy_comment()
