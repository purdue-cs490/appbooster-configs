import grp
import inspect
import os
import pwd
import shutil

import git


def _install_dir(path, perm=None, user=None, group=None, install=False, git_install=None):
    if not path:
        return

    if not os.path.exists(path):
        os.makedirs(path)

    # Clone git repository first, otherwise git will refuse to clone if the
    # folder is not empty
    if git_install:
        git.clone_update_git(git_install, path)

    # Copy directory in files folder
    if install:
        caller_frame = inspect.stack()[2]
        caller_module = inspect.getmodule(caller_frame[0])
        files_root = os.path.join(os.path.dirname(caller_module.__file__), 'files')
        dir_path = os.path.join(files_root, path.lstrip(os.path.sep))

        if os.path.isdir(dir_path):
            for dir_file in os.listdir(dir_path):
                dir_file_path = os.path.join(dir_path, dir_file)
                if os.path.isdir(dir_file):
                    shutil.copytree(dir_file_path, path)
                else:
                    shutil.copy(dir_file_path, path)

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


def _install_file(path, perm=None, user=None, group=None, install=True):
    if not path:
        return

    file_dir = os.path.dirname(path)
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    if install:
        caller_frame = inspect.stack()[2]
        caller_module = inspect.getmodule(caller_frame[0])
        files_root = os.path.join(os.path.dirname(caller_module.__file__), 'files')
        file_path = os.path.join(files_root, path.lstrip(os.path.sep))

        if os.path.isfile(file_path):
            shutil.copy(file_path, path)

    # File installation failed
    if not os.path.isfile(path):
        return

    if perm:
        os.chmod(path, perm)

    if user:
        if not isinstance(user, int):
            user = pwd.getpwnam(user).pw_uid
        os.chown(path, user, -1)

    if group:
        if not isinstance(group, int):
            group = grp.getgrnam(group).gr_gid
        os.chown(path, -1, group)


def install_dirs(dirs):
    for directory in dirs:
        _install_dir(**directory)


def install_files(files):
    for install_file in files:
        _install_file(install_file)
