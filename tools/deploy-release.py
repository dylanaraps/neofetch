#!/usr/bin/env python3
import argparse
import json
import os
import re
import shlex
import stat
import subprocess
import sys
from pathlib import Path
from packaging import version as pv

sys.path.append(str(Path(__file__).parent.parent))

from tools.list_distros import generate_help
from tools.reformat_readme import reformat_readme


def pre_check():
    """
    Check source code status before releasing.
    """
    assert os.path.isfile('./neofetch'), './neofetch doesn\'t exist, you are running this script in the wrong directory'
    assert os.stat('./neofetch').st_mode & stat.S_IEXEC, 'neofetch is not executable'
    assert os.path.islink('./hyfetch/scripts/neowofetch'), 'neowofetch is not a symbolic link'
    # subprocess.check_call(shlex.split('git diff-index --quiet HEAD --'))  # 'Please commit all changes before release'

    subprocess.check_call(shlex.split('shellcheck neofetch'))


def edit_versions(version: str):
    """
    Edit version numbers in hyfetch/constants.py, package.json, and README.md

    Also edits version number of neofetch, but the neofetch version number is separate.

    :param version: Version to release
    """
    # 1. package.json
    path = Path('package.json')
    content = json.loads(path.read_text())
    cur = pv.parse(content['version'])
    assert cur < pv.parse(version), 'Version did not increase'
    content['version'] = version
    path.write_text(json.dumps(content, ensure_ascii=False, indent=2))

    # 2. hyfetch/constants.py
    path = Path('hyfetch/constants.py')
    content = [f"VERSION = '{version}'" if l.startswith('VERSION = ') else l for l in path.read_text().split('\n')]
    path.write_text('\n'.join(content))

    # 3. README.md
    path = Path('README.md')
    content = path.read_text()
    changelog_i = content.index('<!-- CHANGELOG STARTS HERE --->')
    version_i = content.index('###', changelog_i)
    version_end = content.index('\n', version_i)
    content = content[:version_i] + f'### {version}' + content[version_end:]
    path.write_text(content)

    # 4. neofetch script
    path = Path('neofetch')
    lines = path.read_text().split('\n')
    version_i = next(i for i, l in enumerate(lines) if l.startswith('version='))
    nf = pv.parse(lines[version_i].replace('version=', ''))
    new = pv.parse(version)
    nf = f'{nf.major + new.major - cur.major}.{nf.minor + new.minor - cur.minor}.{nf.micro + new.micro - cur.micro}'
    lines[version_i] = f"version={nf}"
    path.write_text('\n'.join(lines))


def finalize_neofetch():
    """
    Finalize current version
    """
    # 1. Update distro list
    path = Path('neofetch')
    content = path.read_text()
    content = re.compile(r'(?<=# Flag:    --ascii_distro\n#\n).*?(?=ascii_distro=)', re.DOTALL)\
        .sub(generate_help(100, '# ') + '\n', content)
    content = re.compile(r"""(?<=Which Distro's ascii art to print\n\n).*?{distro}_small to use them\.""", re.DOTALL)\
        .sub(generate_help(100, ' ' * 32), content)
    path.write_text(content)

    # 2. Regenerate man page
    Path('neofetch.1').write_text(subprocess.check_output(['help2man', './neofetch']).decode())

    # 3. Reformat readme links
    reformat_readme()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='HyFetch Release Utility')
    parser.add_argument('version', help='Version to release')

    args = parser.parse_args()

    pre_check()
    edit_versions(args.version)
    finalize_neofetch()

