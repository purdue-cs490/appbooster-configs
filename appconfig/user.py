import grp
import pwd
import subprocess


def _add_grp(name, gid):
    cmd = ['sudo groupadd -r']
    if gid:
        cmd.extend(['-g', str(gid)])
    cmd.append(name)
    return subprocess.check_call(cmd)


def _add_usr(name, uid, shell):
    cmd = ['sudo useradd -r -N -m']
    if uid:
        cmd.extend(['-u', str(uid)])
    if shell:
        cmd.extend(['-s', shell])
    cmd.extend('-g', name)
    return subprocess.check_call(cmd)


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
