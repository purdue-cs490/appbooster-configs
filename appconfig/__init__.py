from __future__ import print_function

import sys


def host():
    from host import install
    sys.exit(install())


def container():
    from container import install
    sys.exit(install())


def exit_help():
    print('Usage: install.py [command]', file=sys.stderr)
    sys.exit(1)


def main():
    try:
        command_arg = sys.argv[1]
    except IndexError:
        exit_help()

    command = globals().get(command_arg)

    if not command:
        print('???')
    else:
        command()
