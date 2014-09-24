from __future__ import print_function

import grp
import pwd

import command


def _add_grp(name, gid, mod=False):
    if not mod:
        print("Adding group '%s' (%s) ..." % (name, gid))
        cmd = 'groupadd -r'.split()
    else:
        print("Modifying group '%s' to (%s) ..." % (name, gid))
        cmd = 'groupmod'.split()

    if gid:
        cmd.extend(['-g', str(gid)])

    cmd.append(name)

    return command.run(cmd)


def _add_usr(name, uid, gid, groups, shell, mod=False):
    if not mod:
        print("Adding user '%s' (%s:%s) ..." % (name, uid, gid))
        cmd = 'useradd -r -N -m'.split()
    else:
        print("Modifying user '%s' to (%s:%s) ..." % (name, uid, gid))
        cmd = 'usermod'.split()

    if uid:
        cmd.extend(['-u', str(uid)])

    if shell:
        cmd.extend(['-s', shell])

    if gid:
        cmd.extend(['-g', str(gid)])
    else:
        cmd.extend(['-g', name])

    if groups:
        cmd.extend(['-G', ','.join(groups)])

    cmd.append(name)

    return command.run(cmd)


def add_usr_grp(name, uid=None, gid=None, groups=None, shell='/bin/bash'):
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
        _add_usr(name, uid, gid, groups, shell, mod=True)
    except KeyError:
        _add_usr(name, uid, gid, groups, shell)


def add_grp(name, gid=None):
    try:
        grp.getgrnam(name)
        _add_grp(name, gid, mod=True)
    except KeyError:
        _add_grp(name, gid)


def add_users(users):
    for user in users:
        add_usr_grp(**user)


def add_groups(groups):
    for group in groups:
        add_grp(**group)
