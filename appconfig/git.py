import os
import subprocess


def clone_update_git(git_url, path):
    cmd = ('git --git-dir %s' % os.path.join(path, '.git')).split()

    if not os.path.exists(path):
        subprocess.check_call(('git clone %s %s' % (git_url, path)).split())

    fetch_cmd = cmd[:]
    fetch_cmd.append('fetch')
    subprocess.check_call(fetch_cmd)

    reset_cmd = cmd[:]
    reset_cmd.extend('reset --hard master'.split())
    subprocess.check_call(reset_cmd)
