#!/usr/bin/env python

import subprocess
import os


def run():
    script_dir = os.path.dirname(
        os.path.realpath(__file__)
    )  # gets the directory where the script resides
    subprocess.call(
        ["/bin/bash", os.path.join(script_dir, "neofetch")]
    )  # Calling the bash script


if __name__ == "__main__":
    run()
