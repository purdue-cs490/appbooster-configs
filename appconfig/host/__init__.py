from .. import apt
from config import PACKAGES


def install():
    apt.install(PACKAGES)
