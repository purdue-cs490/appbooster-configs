import os

import command


def clone_update_git(git_url, path):
    if not os.path.exists(os.path.join(path, '.git')):
        command.run('git clone %s %s' % (git_url, path))

    cmds = [
        'git fetch origin',
        'git reset --hard origin',
    ]
    for cmd in cmds:
        command.run(cmd, cwd=path)
