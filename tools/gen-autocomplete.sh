#!/usr/bin/env bash

# Echo all commands
set -x

shtab --shell=bash -u hyfetch.main.create_parser > hyfetch/scripts/autocomplete.bash
shtab --shell=zsh -u hyfetch.main.create_parser > hyfetch/scripts/autocomplete.zsh
shtab --shell=tcsh -u hyfetch.main.create_parser > hyfetch/scripts/autocomplete.csh
