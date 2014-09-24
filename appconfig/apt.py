import subprocess


def update():
    cmd = 'sudo apt-get update'.split()
    return subprocess.check_call(cmd)


def install(packages):
    cmd = 'sudo apt-get -y install'.split()
    cmd.extend(packages)
    return subprocess.check_call(cmd)
