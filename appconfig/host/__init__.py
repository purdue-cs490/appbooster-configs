from .. import apt, user
from config import PACKAGES, USERS


def install():
    apt.update()
    apt.install(PACKAGES)

    user.add_users(USERS)
