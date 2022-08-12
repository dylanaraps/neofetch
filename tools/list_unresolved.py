#!/usr/bin/env python3
import math
import os
import shlex
from collections import Counter
from pathlib import Path
from subprocess import check_output

from github import Github
from github.PullRequest import PullRequest
import ruamel.yaml as yaml
from hypy_utils.tqdm_utils import tq, pmap, tmap


def obtain_resolved():
    """
    Obtain a list of resolved issues.
    """
    prefix = 'dylanaraps/neofetch#'
    commits = check_output(shlex.split('git log --pretty=format:"%s"')).decode().strip().split('\n')
    commits = [(c, c.find(prefix)) for c in commits]
    commits = [(c, i+len(prefix)) for c, i in commits if i != -1]
    return sorted([int(c[i:c.find(' ', i)]) for c, i in commits])


if __name__ == '__main__':
    # Obtain a list of resolved issues
    resolved = set(obtain_resolved())

    # Read the ignore-list
    with open(Path(__file__).parent / "pull_request_markings.yaml") as stream:
        ignore_list: dict[int, str] = yaml.safe_load(stream)['IgnoreList']
        ignore_list.update({r: 'merged' for r in resolved})

    # Obtain a list of open issues
    g = Github(per_page=100, login_or_token=os.environ.get('GH_TOKEN'))
    repo = g.get_repo('dylanaraps/neofetch')
    pager = repo.get_pulls(state='all')

    # Filter only unresolved issues
    pages = list(range(math.ceil(pager.totalCount // 100) + 1))
    pulls: list[list[PullRequest]] = tmap(pager.get_page, pages, desc='Crawling pull requests...', unit='page')
    pulls: set[PullRequest] = {p for lst in pulls for p in lst}
    unresolved: set[PullRequest] = {p for p in pulls if p.number not in resolved and p.number not in ignore_list}

    # Filter merged / closed
    draft = {p for p in unresolved if p.draft}
    unresolved -= draft
    merged = {p for p in unresolved if p.merged_at}
    unresolved -= merged
    closed = {p for p in unresolved if p.state == 'closed'}
    unresolved -= closed

    ignore_counter = Counter(ignore_list.values())
    hyfetch_merged = ignore_counter.pop('merged')
    print(f'Pull Request Statistics:')
    print(f'> {hyfetch_merged} PRs merged by HyFetch')
    print('\n'.join(f'> {c} PRs closed as {v} by HyFetch' for v, c in sorted(ignore_counter.items(), key=lambda x: -x[1])))
    print()
    print(f'> {len(draft)} PR drafts')
    print(f'> {len(merged)} PRs merged by neofetch')
    print(f'> {len(closed)} PRs closed without merging')
    print()
    print(f'> {len(unresolved)} open PRs that needs to be addressed:')
    print()

    opened = sorted(list(unresolved), key=lambda p: p.number)

    # Print unresolved issues
    print('\n'.join(f'[{p.number}] {p.title} {p.html_url}' for p in opened))
