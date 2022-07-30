#!/usr/bin/env python3
import argparse
import os

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

    # Fetch head branch
    print()
    print('Fetching head branch...')
    os.system(f'git fetch https://github.com/{head} {head_br}')

    # Merge head branch
    print()
    print('Merging fetch_head...')
    os.system(f'git merge FETCH_HEAD --no-ff --no-edit '
              f'-m "[PR] {upstream}#{pr} from {user} - {info["title"]}" '
              f'-m "Upstream PR: https://github.com/{upstream}/pull/{pr}  \nThanks to @{user}"')

    # Create GitHub Pull Request
    # print()
    # print('Creating pull request...')
    # g = Github(gh_token)
    # repo = g.get_repo(my_fork)
    # pr = repo.create_pull(title=info['title'], body=f"Upstream PR: https://github.com/{upstream}/pull/{pr}  \nThanks to: @{info['user']['login']}",
    #                       base=my_base, head=head_lbl)
    # print(pr)
