import os
from subprocess import check_output

import pkg_resources


def get_command_path() -> str:
    """
    Get the absolute path of the neofetch command

    :return: Command path
    """
    return pkg_resources.resource_filename(__name__, 'scripts/neofetch_mod.sh')


def get_distro_ascii_lines() -> int:
    """
    Get how many lines are in the distro ascii

    :return: Number of lines
    """
    out = check_output([get_command_path(), "print_ascii"])
    return len(out.decode().strip().split('\n'))
