import subprocess


def update():
    cmd = 'apt-get update'.split()
    return subprocess.check_call(cmd)


def install(packages):
    cmd = 'DEBIAN_FRONTEND=noninteractive apt-get -y install'.split()
    cmd.extend(packages)
    return subprocess.check_call(cmd)
