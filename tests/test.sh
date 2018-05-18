#!/usr/bin/env bash
#
# Run all tests.

./test_misc.sh

[[ -f /tmp/err ]] || exit 0 && { rm /tmp/err; exit 1; }
