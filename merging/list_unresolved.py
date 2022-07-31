import shlex
from pathlib import Path
from subprocess import check_output

from github import Github
from github.PullRequest import PullRequest
import ruamel.yaml as yaml


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
        ignore_list = yaml.safe_load(stream)['IgnoreList']

    # Obtain a list of open issues
    g = Github(per_page=100)
    repo = g.get_repo('dylanaraps/neofetch')
    pager = repo.get_pulls(state='open')

    # Filter only unresolved issues
    unresolved: list[PullRequest] = []
    for i in range(10000000):
        pulls: list[PullRequest] = pager.get_page(i)
        if len(pulls) == 0:
            break

        unresolved += [p for p in pulls if p.number not in resolved and p.number not in ignore_list and not p.draft]
        if len(unresolved) > 50:
            break

    unresolved.sort(key=lambda p: p.number)

    # Print unresolved issues
    print('\n'.join(f'[{p.number}] {p.title} {p.html_url}' for p in unresolved))
