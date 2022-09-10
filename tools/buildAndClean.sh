#!/usr/bin/env bash

# Stop on error
set -e

# Remove old build
rm -rf ../dist/*
rm -rf ../build/*

# Build
cd ..
python setup.py sdist bdist_wheel
