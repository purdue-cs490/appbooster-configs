from __future__ import print_function

import grp
import pwd

import command


def _add_grp(name, gid):
    print("Adding group (%s) ..." % gid)

    cmd = 'groupadd -r'.split()

    if gid:
        cmd.extend(['-g', str(gid)])

    cmd.append(name)

    return command.run(cmd)


def _add_usr(name, uid, gid, shell):
    print("Adding user '%s' (%s:%s) ..." % (name, uid, gid))

    cmd = 'useradd -r -N -m'.split()

    if uid:
        cmd.extend(['-u', str(uid)])

    if shell:
        cmd.extend(['-s', shell])

    if gid:
        cmd.extend(['-g', str(gid)])
    else:
        cmd.extend(['-g', name])

    cmd.append(name)

    return command.run(cmd)


def add_usr_grp(name, uid=None, gid=None, shell='/bin/bash'):
    if isinstance(gid, int):
        gid_check_func = grp.getgrgid
    else:
        gid_check_func = grp.getgrnam

    try:
        gid_check_func(gid)
    except KeyError:
        _add_grp(name, gid)

    try:
        pwd.getpwnam(name)
    except KeyError:
        _add_usr(name, uid, gid, shell)


def add_users(users):
    for user in users:
        add_usr_grp(**user)
