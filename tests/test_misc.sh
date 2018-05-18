#!/usr/bin/env bash
#
# Test misc functions.

source test_util.sh
source ../neofetch

# Tests only work on Linux for now.
os="Linux"


test_convert_time() {
    # 24 hour time.
    result="$(convert_time "2016" "04" "14" "23:50")"
    assert_equals "$result" "Thu 14 Apr 2016 23:50"

    # 12 hour time.
    install_time_format="12h"
    result="$(convert_time "2016" "04" "14" "23:50")"
    assert_equals "$result" "Thu 14 Apr 2016 11:50 PM"
}

test_get_ppid() {
    result="$(trim "$(get_ppid "1")")"
    assert_equals "$result" "0"
}

test_get_process_name() {
    result="$(get_process_name "1")"
    assert_equals "$result" "systemd"
}


printf "%s\\n" "Test MISC functions."
test_convert_time
test_get_ppid
test_get_process_name
