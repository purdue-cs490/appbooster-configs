from __future__ import print_function

from .. import apt, files, user
from config import DIRS, PACKAGES, USERS


def install():
    print('Installing packages...')
    apt.update()
    apt.install(PACKAGES)

    print('Adding users...')
    user.add_users(USERS)

    print('Installing directories...')
    files.install_dirs(DIRS)
