from __future__ import annotations

import os
import platform
import signal
import sys
import termios
import tty

from .color_util import RGB, AnsiMode


class OSCException(Exception):
    pass


def unix_detect_ansi_mode() -> AnsiMode | None:
    """
    Translated from Termenv's ColorProfile():
    https://github.com/muesli/termenv/blob/42ca574de3e99a262e1724d2fb8daa1aea68a5b9/termenv_unix.go#L23

    :return: Ansi mode
    """
    if not sys.stdout.isatty():
        return 'ansi'

    term = os.environ.get('TERM')
    color_term = os.environ.get('COLORTERM')

    if color_term == 'truecolor' or color_term == '24bit':
        if term.startswith('screen') and os.environ.get('TERM_PROGRAM') != 'tmux':
            return '8bit'
        return 'rgb'

    elif color_term == 'true' or color_term == 'yes':
        return '8bit'

    if term == 'xterm-kitty':
        return 'rgb'
    elif term == 'linux':
        return 'ansi'

    if '256color' in term:
        return 'rgb'
    if 'color' in term:
        return '8bit'
    if 'ansi' in term:
        return 'ansi'

    return None


def windows_detect_ansi_mode() -> AnsiMode | None:
    """
    Translated from Termenv's ColorProfile():
    https://github.com/muesli/termenv/blob/42ca574de3e99a262e1724d2fb8daa1aea68a5b9/termenv_windows.go#L13

    :return: Ansi mode
    """
    if not sys.stdout.isatty():
        return 'ansi'

    if os.environ.get("ConEmuANSI") == "ON":
        return 'rgb'

    release, _, build = map(int, platform.version().split('.'))
    if build < 10586 or release < 10:
        # No ANSI support before Windows 10 build 10586.
        if os.environ.get('ANSICON'):
            conv = os.environ.get('ANSICON_VER')
            if int(conv) < 181:
                return 'ansi'
            return '8bit'
        return 'ansi'

    if build < 14931:
        # No true color support before build 14931.
        return '8bit'

    return 'rgb'


def detect_ansi_mode() -> AnsiMode | None:
    system = platform.system().lower()
    if system.startswith("linux") or system.startswith("darwin"):
        return unix_detect_ansi_mode()
    if system.startswith("windows"):
        return windows_detect_ansi_mode()
    return None


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


