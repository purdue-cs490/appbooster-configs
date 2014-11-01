import command


def update():
    cmd = 'apt-get update'
    return command.run(cmd)


def upgrade():
    cmd = 'apt-get upgrade -y'
    return command.run(cmd)


def install(packages):
    cmd = 'apt-get -y install'.split()
    cmd.extend(packages)

    env = {
        'DEBIAN_FRONTEND': 'noninteractive',
    }

    return command.run(cmd, env=env)
