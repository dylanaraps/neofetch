#!/usr/bin/env python3
import argparse
import json
import os
import re
import shlex
import stat
import subprocess
from pathlib import Path

from packaging import version as pv

from tools.list_distros import generate_help, export_distros
from tools.reformat_readme import reformat_readme

NEOFETCH_NEW_VERSION = ""


def pre_check():
    """
    Check source code status before releasing.
    """
    assert os.path.isfile('./neofetch'), './neofetch doesn\'t exist, you are running this script in the wrong directory'
    assert os.stat('./neofetch').st_mode & stat.S_IEXEC, 'neofetch is not executable'
    assert os.path.islink('./hyfetch/scripts/neowofetch'), 'neowofetch is not a symbolic link'
    # subprocess.check_call(shlex.split('git diff-index --quiet HEAD --'))  # 'Please commit all changes before release'

    print('Running shellcheck... (This may take a while)')
    subprocess.check_call(shlex.split('shellcheck neofetch'))


def edit_versions(version: str):
    """
    Edit version numbers in hyfetch/constants.py, package.json, and README.md

    Also edits version number of neofetch, but the neofetch version number is separate.

    :param version: Version to release
    """
    # 1. package.json
    print('Editing package.json...')
    path = Path('package.json')
    content = json.loads(path.read_text())
    cur = pv.parse(content['version'])
    assert cur < pv.parse(version), 'Version did not increase'
    content['version'] = version
    path.write_text(json.dumps(content, ensure_ascii=False, indent=2))

    # 2. hyfetch/constants.py
    print('Editing hyfetch/__version__.py...')
    path = Path('hyfetch/__version__.py')
    content = [f"VERSION = '{version}'" if l.startswith('VERSION = ') else l for l in path.read_text().split('\n')]
    path.write_text('\n'.join(content))

    # 3. README.md
    print('Editing README.md...')
    path = Path('README.md')
    content = path.read_text()
    changelog_token = '<!-- CHANGELOG STARTS HERE --->'
    changelog_i = content.index(changelog_token) + len(changelog_token)
    content = content[:changelog_i] + f'\n\n### {version}' + content[changelog_i:]
    path.write_text(content)

    # 4. neofetch script
    print('Editing neofetch...')
    path = Path('neofetch')
    lines = path.read_text().replace("\t", "    ").split('\n')
    version_i = next(i for i, l in enumerate(lines) if l.startswith('version='))
    nf = pv.parse(lines[version_i].replace('version=', ''))
    new = pv.parse(version)
    nf = f'{nf.major + new.major - cur.major}.{nf.minor + new.minor - cur.minor}.{nf.micro + new.micro - cur.micro}'
    lines[version_i] = f"version={nf}"
    path.write_text('\n'.join(lines))

    global NEOFETCH_NEW_VERSION
    NEOFETCH_NEW_VERSION = nf


def finalize_neofetch():
    """
    Finalize current version
    """
    # 1. Update distro list
    print('Updating distro list in neofetch...')
    path = Path('neofetch')
    content = path.read_text()
    content = re.compile(r'(?<=# Flag:    --ascii_distro\n#\n).*?(?=ascii_distro=)', re.DOTALL)\
        .sub(generate_help(100, '# ') + '\n', content)
    content = re.compile(r"""(?<=Which Distro's ascii art to print\n\n).*?{distro}_small to use them\.""", re.DOTALL)\
        .sub(generate_help(100, ' ' * 32), content)
    path.write_text(content)

    # 2. Regenerate man page
    print('Regenerating neofetch man page...')
    Path('neofetch.1').write_text(subprocess.check_output(['help2man', './neofetch']).decode())

    # 3. Reformat readme links
    print('Reformatting readme links...')
    reformat_readme()


def post_check():
    """
    Check after changes are made
    """
    print('Running shellcheck... (This may take a while)')
    subprocess.check_call(shlex.split('shellcheck neofetch'))


def create_release(v: str):
    """
    Create release commit and tag
    """
    print('Committing changes...')

    # 1. Add files
    subprocess.check_call(['git', 'add', 'hyfetch/__version__.py', 'neofetch', 'neofetch.1', 'package.json', 'README.md',
                           'hyfetch/distros/*'])

    # 2. Commit
    subprocess.check_call(['git', 'commit', '-m', f'[U] Release {v}'])

    # 3. Create tag
    subprocess.check_call(['git', 'tag', v])
    subprocess.check_call(['git', 'tag', f'neofetch-{NEOFETCH_NEW_VERSION}'])

    i = input('Please check the commit is correct. Press y to continue or any other key to cancel.')
    assert i == 'y'

    # 4. Push
    print('Pushing commits...')
    subprocess.check_call(['git', 'push'])
    subprocess.check_call(['git', 'push', 'origin', v, f'neofetch-{NEOFETCH_NEW_VERSION}'])


def deploy():
    """
    Deploy release to pip and npm
    """
    print('Deploying to pypi...')
    subprocess.check_call(['bash', 'tools/deploy.sh'])
    print('Done!')

    print('Deploying to npm...')
    otp = input('Please provide 2FA OTP for NPM: ')
    subprocess.check_call(['npm', 'publish', '--otp', otp])
    print('Done!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HyFetch Release Utility')
    parser.add_argument('version', help='Version to release')

    args = parser.parse_args()

    pre_check()
    export_distros()
    edit_versions(args.version)
    finalize_neofetch()
    post_check()
    create_release(args.version)
    deploy()

