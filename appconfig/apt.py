import os
import subprocess


def update():
    cmd = 'apt-get update'.split()
    return subprocess.check_call(cmd)


def install(packages):
    cmd = 'apt-get -y install'.split()
    cmd.extend(packages)

    env = {}
    env.update(os.environ)
    env['DEBIAN_FRONTEND'] = 'noninteractive'

    return subprocess.check_call(cmd, env=env)
