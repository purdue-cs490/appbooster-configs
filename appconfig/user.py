import grp
import pwd

import command


def _add_grp(name, gid):
    cmd = 'groupadd -r'.split()
    if gid:
        cmd.extend(['-g', str(gid)])
    cmd.append(name)

    return command.run(cmd)


def _add_usr(name, uid, shell):
    cmd = 'useradd -r -N -m'.split()
    if uid:
        cmd.extend(['-u', str(uid)])
    if shell:
        cmd.extend(['-s', shell])
    cmd.extend(['-g', name])
    cmd.append(name)

    return command.run(cmd)


def add_usr_grp(name, uid=None, gid=None, shell='/bin/bash'):
    try:
        grp.getgrnam(name)
    except KeyError:
        _add_grp(name, gid)

    try:
        pwd.getpwnam(name)
    except KeyError:
        _add_usr(name, uid, shell)


def add_users(users):
    for user in users:
        add_usr_grp(**user)
