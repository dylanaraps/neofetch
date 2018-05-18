#!/usr/bin/env bash
#
# Test util functions.

assert_equals() {
    # Test equality.
    local status
    [[ "$1" == "$2" ]] && status="✔"
    printf "%s\\n" "  ${status:-✖} : ${FUNCNAME[1]}"
    [[ "$1" == "$2" ]] || { :>/tmp/err; return 1; } && return 0
}
