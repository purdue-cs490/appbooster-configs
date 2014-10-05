from __future__ import print_function

from .. import apt
from .. import files
from .. import user
from .. import command

from config import *


def install():
    try:
        print("\033[32mInstalling packages...\033[0m")
        apt.update()
        apt.install(PACKAGES)

        print("\033[32mAdding users and groups ...\033[0m")
        user.add_groups(GROUPS)
        user.add_users(USERS)

        print("\033[32mInstalling directories...\033[0m")
        files.install_dirs(DIRS)

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

        print()
        print("\033[32mSucceed!\033[0m")
    except KeyboardInterrupt:
        pass
    except Exception:
        print("\033[31;1mError:\033[0m")
        raise
