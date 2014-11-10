from __future__ import print_function

import os

import apt
import files
import user

from config import *


def install():
    if not os.geteuid() == 0:
        print("\033[31;1mMust be run as root\033[0m")
        return 2

    try:
        print("\033[32mInstalling packages...\033[0m")
        apt.update()
        apt.upgrade()
        apt.install(PACKAGES)

        print("\033[32mAdding users and groups ...\033[0m")
        user.add_groups(GROUPS)
        user.add_users(USERS)

        print("\033[32mInstalling directories...\033[0m")
        files.install_dirs(DIRS)

        print("\033[32mInstalling files...\033[0m")
        files.install_files(FILES)

        print("\033[32mSucceed!\033[0m")
    except KeyboardInterrupt:
        pass
    except Exception:
        print("\033[31;1mError:\033[0m")
        raise
