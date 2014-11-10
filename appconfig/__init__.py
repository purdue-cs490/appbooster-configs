"""Usage: %s [role]

roles:
    host
    container
"""

from __future__ import print_function

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


def host():
    from host import install
    return install()


def container():
    from container import install
    return install()


def exit_help():
    print(__doc__ % sys.argv[0], file=sys.stderr)
    return 1


def main():
    if len(sys.argv) != 2:
        return exit_help()

    command_arg = sys.argv[1]
    command = globals().get(command_arg)

    if not command:
        print('???')
    else:
        return command()
