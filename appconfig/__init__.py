from __future__ import print_function

import sys


def _err_print(s):
    print(s, file=sys.stderr)


def host():
    from host import install
    return install()


def container():
    from container import install
    return install()


def exit_help():
    _err_print('Usage: %s [role]' % sys.argv[0])
    _err_print('')
    _err_print('roles:')
    _err_print('    host')
    _err_print('    container')
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
