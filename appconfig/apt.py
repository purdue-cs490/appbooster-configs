import subprocess


def update():
    cmd = 'sudo apt-get update'.split()
    return subprocess.check_call(cmd)


def install(packages):
    cmd = 'sudo DEBIAN_FRONTEND=noninteractive apt-get -y install'.split()
    cmd.extend(packages)
    return subprocess.check_call(cmd)
