from __future__ import print_function

import os

from .. import apt
from .. import files
from .. import user
from .. import command

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

        print("\033[32mUpdating grub configs...\033[0m")
        command.run('update-grub')

        print("\033[32mSetting up MySQL...\033[0m")

        print("\033[32mSetting up Git server...\033[0m")
        command.run_sudo_script("""
            set -e
            if [ ! -f ~/.ssh/id_rsa ]; then
                ssh-keygen -q -f /home/appbooster/.ssh/id_rsa -N ""
            fi
            """, user="appbooster")
        command.run_sudo_script("""
            set -e
            if [ ! -d /home/git/repositories/gitolite-admin.git ]; then
                cd ~
                gitolite setup -pk /home/appbooster/.ssh/id_rsa.pub -a appbooster
            fi
            """, user="git")

        print("\033[32mSetting up appbooster host...\033[0m")
        command.run_sudo_script("""
            set -e
            cd /home/appbooster/host
            virtualenv --no-site-packages ENV
            source ENV/bin/activate
            pip install -r requirements.txt
            export ENVIRONMENT=prod
            ./manage.py migrate
            deactivate
            """, user="appbooster")

        print("\033[32mRestarting services...\033[0m")
        command.run_script("""
            systemctl reload uwsgi
            systemctl reload nginx
            """)

        print("\033[32mSucceed!\033[0m")
    except KeyboardInterrupt:
        pass
    except Exception:
        print("\033[31;1mError:\033[0m")
        raise
