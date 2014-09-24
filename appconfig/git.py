import os

import command


def clone_update_git(git_url, path):
    cmd = ('git --git-dir %s' % os.path.join(path, '.git')).split()

    if not os.path.exists(os.path.join(path, '.git')):
        command.run('git clone %s %s' % (git_url, path))

    fetch_cmd = cmd[:]
    fetch_cmd.extend('fetch origin'.split())
    command.run(fetch_cmd)

    reset_cmd = cmd[:]
    reset_cmd.extend('reset --hard master'.split())
    command.run(reset_cmd)
