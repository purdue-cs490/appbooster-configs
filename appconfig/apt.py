import subprocess


def install(packages):
    cmd = 'sudo apt-get -y install'.split().extend(packages)
    return subprocess.check_call(cmd)
