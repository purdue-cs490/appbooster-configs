import os

import command


def clone_update_git(git_url, path):
    if not os.path.exists(os.path.join(path, '.git')):
        command.run('git clone %s %s' % (git_url, path))

    cmds = [
        'git fetch',
        'git reset --hard',
    ]
    for cmd in cmds:
        command.run(cmd, cwd=path)
