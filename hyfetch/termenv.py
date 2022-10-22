from __future__ import annotations

import os
import signal
import sys
import termios
import tty

from hyfetch.color_util import RGB


class OSCException(Exception):
    pass


def unix_read_osc(seq: int) -> str:
    # screen/tmux can't support OSC, because they can be connected to multiple
    # terminals concurrently.
    term = os.environ.get('TERM')
    if term.startswith("screen") or term.startswith("tmux"):
        raise OSCException("Screen/tmux not supported")

    t = sys.stdout
    if not t.isatty():
        raise OSCException("Not a tty")

    fd = sys.stdin.fileno()

    # Set raw mode
    settings = termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())

    # first, send OSC query, which is ignored by terminal which do not support it
    t.write(f"\x1b]{seq};?\x1b\\")
    t.flush()

    # Since python's select.select is behaving differently than Unix.select, we can't use it to
    # monitor if input is available (https://stackoverflow.com/q/74160774/7346633).
    # My temporary solution is to set a timeout of 0.01s and read as much as possible until the timeout.
    def handler(signum, frame):
        raise IOError()
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, 0.01, 0.0)
    code = ""
    try:
        while 1:
            code += sys.stdin.read(1)
    except IOError:
        pass

    # Reset terminal back to normal mode (previously set to raw mode)
    termios.tcsetattr(fd, termios.TCSADRAIN, settings)

    # Validate output
    if not code:
        raise OSCException("No response received")

    start = f"\x1b]{seq};"
    if not code.startswith(start):
        raise OSCException("Received response is not an OSC response")
    code = code.lstrip(start).rstrip("\x1b\\")

    return code


def get_background_color() -> RGB | None:
    try:
        osc = unix_read_osc(11).lstrip("rgb:")
        return RGB.from_hex(''.join([v[:2] for v in osc.split('/')]))
    except Exception:
        return None


if __name__ == '__main__':
    print(get_background_color())


