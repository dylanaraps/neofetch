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

http = requests.Session()
if 'GH_TOKEN' in os.environ:
    print('Token loaded')
    http.headers['Authorization'] = f'token {os.environ["GH_TOKEN"]}'


def copy_comment():
    # Get commit SHA
    sha = check_output(shlex.split('git rev-parse --short HEAD')).decode().strip()

    # Copy comment to clipboard
    comment = f"""
Thank you for your contribution! 

This PR is [merged into hyfetch](https://github.com/hykilpikonna/hyfetch/commit/{sha}) since this repo (dylanaraps/neofetch) seems no longer maintained.

[HyFetch](https://github.com/hykilpikonna/hyfetch) is a fork of neofetch with LGBTQ pride flags, but the repo also maintains an updated version of the original neofetch, addressing many pull requests that are not merged in the original repo.

Read the ["Running Updated Original Neofetch" section](https://github.com/hykilpikonna/hyfetch#running-updated-original-neofetch) for more info!
    """
    pyperclip.copy(comment.strip())
    print()
    print('Done!')
    print('Comment response copied to clipboard.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Helper for accepting upstream pull requests')
    parser.add_argument('pull', type=int, help='Pull request number')
    args = parser.parse_args()
    pr = args.pull

    print(f'Accepting pull request {pr}...')

    # Fetch original pr's information
    info = http.get(f'https://api.github.com/repos/{upstream}/pulls/{pr}').json()
    user = info['user']['login']

    # Fetch commit information
    commits = http.get(f'https://api.github.com/repos/{upstream}/pulls/{pr}/commits').json()
    author = commits[0]['commit']['author']

    # Create commit message
    title = info["title"].replace('"', '\\"')
    msg = (f'-m "[PR] {upstream}#{pr} from {user} - {title}" '
           f'-m "Upstream PR: https://github.com/{upstream}/pull/{pr}  \n'
           f'Thanks to @{user}\n\n'
           f'Co-authored-by: {author["name"]} <{author["email"]}>"')

    # head could be null, if the pr repo is deleted
    if info['head'] is None or info['head']['repo'] is None:
        print(f'Original repo is deleted. Please manually merge.')
        input('Press any key to continue when the changes are made...')

        # Commit with merge
        print()
        print('Committing merge...')
        os.system(f'git commit -a {msg}')

    # Automatically merge
    else:
        head = info['head']['repo']['full_name']
        head_br = info['head']['ref']
        head_lbl = info['head']['label']
        print()
        print('Original Pull Request Info:')
        print('> State:', info['state'])
        print('> Title:', info['title'])
        print('> User:', user)
        print('> Created:', info['created_at'])
        print('> Head:', head, head_br, head_lbl)

        # Fetch head branch
        print()
        print('Fetching head branch...')
        os.system(f'git fetch https://github.com/{head} {head_br}')

        # Merge head branch
        print()
        print('Merging fetch_head...')
        os.system(f'git merge FETCH_HEAD --no-ff --no-edit {msg}')

    # Push
    print()
    print('Pushing...')
    os.system('git push')

    copy_comment()
