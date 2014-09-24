import subprocess


def install(packages):
    cmd = 'sudo apt-get -y install'.split()
    cmd.extend(packages)
    return subprocess.check_call(cmd)
