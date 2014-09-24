import os
import subprocess


def run(cmd, env=None):
    if isinstance(cmd, str):
        cmd = cmd.split()

    envs = {}
    envs.update(os.environ)
    if env:
        envs.update(env)

    return subprocess.check_call(cmd, env=envs)


def run_script(script):
    return subprocess.check_call(['/bin/bash', '-c', script])


def run_sudo_script(script, user=None):
    if user:
        cmd = ['/usr/bin/sudo', '-u', user]
    else:
        cmd = ['/usr/bin/sudo']

    cmd.extend(['/bin/bash', '-c', script])

    return subprocess.check_call(cmd)
