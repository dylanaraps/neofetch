#!/usr/bin/env bash

# Echo all commands
set -x

shtab --shell=bash hyfetch.main.create_parser > hyfetch/scripts/autocomplete.bash
shtab --shell=zsh hyfetch.main.create_parser > hyfetch/scripts/autocomplete.zsh
shtab --shell=tcsh hyfetch.main.create_parser > hyfetch/scripts/autocomplete.csh
