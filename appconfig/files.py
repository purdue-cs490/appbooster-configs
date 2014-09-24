import grp
import os
import pwd

import git


def install_dir(directory):
    dir_path = directory.get('path')
    if not dir_path:
        return

    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    dir_git = directory.get('git')
    if dir_git:
        git.clone_update_git(dir_git, dir_path)

    dir_perm = directory.get('perm')
    if dir_perm:
        os.chmod(dir_path, dir_perm)

    dir_user = directory.get('user')
    if dir_user:
        if not isinstance(dir_user, int):
            dir_user = pwd.getpwnam(dir_user).pw_uid
        os.chown(dir_path, dir_user, -1)
        for dir_root, dirnames, filenames in os.walk(dir_path):
            for d in dirnames:
                os.chown(os.path.join(dir_root, d), dir_user, -1)
            for f in filenames:
                os.chown(os.path.join(dir_root, f), dir_user, -1)

    dir_group = directory.get('group')
    if dir_group:
        if not isinstance(dir_group, int):
            dir_group = grp.getgrnam(dir_group).gr_gid
        os.chown(dir_path, -1, dir_group)
        for dir_root, dirnames, filenames in os.walk(dir_path):
            for d in dirnames:
                os.chown(os.path.join(dir_root, d), -1, dir_group)
            for f in filenames:
                os.chown(os.path.join(dir_root, f), -1, dir_group)


def install_dirs(dirs):
    for directory in dirs:
        install_dir(directory)
