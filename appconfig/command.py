import os
import subprocess


def run(cmd, check=True, env=None, cwd=None):
    if isinstance(cmd, str):
        cmd = cmd.split()

    envs = {}
    envs.update(os.environ)
    if env:
        envs.update(env)

    if check:
        return subprocess.check_call(cmd, env=envs, cwd=cwd)
    else:
        return subprocess.call(cmd, env=envs, cwd=cwd)


def run_script(script, **kwargs):
    return run(['/bin/bash', '-c', script], **kwargs)


def run_sudo_script(script, user=None, **kwargs):
    if user:
        cmd = ['/usr/bin/sudo', '-u', user]
    else:
        cmd = ['/usr/bin/sudo']

    cmd.extend(['/bin/bash', '-c', script])

    return run(cmd, **kwargs)
