from __future__ import print_function

from .. import apt
from .. import files
from .. import user
from .. import command

from config import DIRS, PACKAGES, USERS


def install():
    print('Installing packages...')
    apt.update()
    apt.install(PACKAGES)

    print('Adding users...')
    user.add_users(USERS)

    print('Installing directories...')
    files.install_dirs(DIRS)

    print('Setting up appbooster host...')
    command.run_sudo_script("""
        cd /home/appbooster/host
        virtualenv --no-site-packages ENV
        source ENV
        pip install -r requirements.txt
    """, user="appbooster")
