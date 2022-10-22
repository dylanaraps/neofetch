import os
import signal
import sys
import termios
import tty


class OSCException(Exception):
    pass


def read_osc(seq: int) -> str:
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
    t.write(f"\033]{seq};?\033\\")

    # then, query cursor position, should be supported by all terminals
    t.write("\033[6n")
    t.flush()

    # code = ""
    # while 1:
    #     rlist, w, e = select.select([fd], [], [], 0.1)
    #     print(rlist, w, e)
    #     if not rlist:
    #         break
    #     code += sys.stdin.read(1)

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

    return code


if __name__ == '__main__':
    print(repr(read_osc(11)))


