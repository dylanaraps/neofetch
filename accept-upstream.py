#!/usr/bin/env python3
import argparse
import os
import shlex
from subprocess import check_output

import pyperclip
import requests
from github import Github

upstream = 'dylanaraps/neofetch'
my_fork = 'hykilpikonna/hyfetch'
my_base = 'master'
# gh_token = os.environ['GH_TOKEN']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Helper for accepting upstream pull requests')
    parser.add_argument('pull', type=int, help='Pull request number')
    args = parser.parse_args()
    pr = args.pull

    print(f'Accepting pull request {pr}...')

    # Fetch original pr's information
    info = requests.get(f'https://api.github.com/repos/{upstream}/pulls/{pr}').json()
    # print(info)
    head = info['head']['repo']['full_name']
    head_br = info['head']['ref']
    head_lbl = info['head']['label']
    user = info['user']['login']
    print()
    print('Original Pull Request Info:')
    print('> State:', info['state'])
    print('> Title:', info['title'])
    print('> User:', user)
    print('> Created:', info['created_at'])
    print('> Head:', head, head_br, head_lbl)

    # Fetch commit information
    commits = requests.get(f'https://api.github.com/repos/{upstream}/pulls/{pr}/commits').json()
    author = commits[0]['commit']['author']

    # Fetch head branch
    print()
    print('Fetching head branch...')
    os.system(f'git fetch https://github.com/{head} {head_br}')

    # Merge head branch
    print()
    print('Merging fetch_head...')
    os.system(f'git merge FETCH_HEAD --no-ff --no-edit '
              f'-m "[PR] {upstream}#{pr} from {user} - {info["title"]}" '
              f'-m "Upstream PR: https://github.com/{upstream}/pull/{pr}  \n'
              f'Thanks to @{user}\n\n'
              f'Co-authored-by: {author["name"]} <{author["email"]}>"')

    # Get commit SHA
    sha = check_output(shlex.split('git rev-parse --short HEAD')).decode().strip()

    # Copy comment to clipboard
    comment = f"""
Thank you for your contribution! 

This PR is [merged into hyfetch](https://github.com/hykilpikonna/hyfetch/commit/{sha}) since this repo (dylanaraps/neofetch) seems no longer maintained.

[HyFetch](https://github.com/hykilpikonna/hyfetch) is a fork of neofetch with LGBTQ pride flags, but the repo also serves as an updated version of neofetch, addressing many pull requests that are not merged in the original repo.
    """
    pyperclip.copy(comment.strip())
    print()
    print('Done!')
    print('Comment response copied to clipboard.')
