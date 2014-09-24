from .. import apt
from config import PACKAGES


def install():
    apt.update()
    apt.install(PACKAGES)
