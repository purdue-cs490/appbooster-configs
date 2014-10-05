import grp
import os
import pwd

import git


def install_dir(path, perm=None, user=None, group=None, git_install=None):
    if not path:
        return

    if not os.path.exists(path):
        os.makedirs(path)

    if git_install:
        git.clone_update_git(git_install, path)

    if perm:
        os.chmod(path, perm)

    if user:
        if not isinstance(user, int):
            user = pwd.getpwnam(user).pw_uid
        os.chown(path, user, -1)
        for dir_root, dirnames, filenames in os.walk(path):
            for d in dirnames:
                os.chown(os.path.join(dir_root, d), user, -1)
            for f in filenames:
                os.chown(os.path.join(dir_root, f), user, -1)

    if group:
        if not isinstance(group, int):
            group = grp.getgrnam(group).gr_gid
        os.chown(path, -1, group)
        for dir_root, dirnames, filenames in os.walk(path):
            for d in dirnames:
                os.chown(os.path.join(dir_root, d), -1, group)
            for f in filenames:
                os.chown(os.path.join(dir_root, f), -1, group)


def install_dirs(dirs):
    for directory in dirs:
        install_dir(**directory)
