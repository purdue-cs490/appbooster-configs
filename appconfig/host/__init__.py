from __future__ import print_function

from .. import apt, user
from config import PACKAGES, USERS


def install():
    print('Installing packages...')
    apt.update()
    apt.install(PACKAGES)

    print('Adding users...')
    user.add_users(USERS)
