# List of packages to be installed
PACKAGES = [
    'sudo',
    'vim',
    'git',
    'nginx',
    'mysql-server-5.5',
    'libmysqlclient-dev',
    'docker.io',
    'python2.7',
    'libpython2.7-dev',
    'python-pip',
    'python-virtualenv',
    'uwsgi',
]

# List of users to be added
USERS = [
    {
        'name': 'appbooster',
        'uid': 800,
        'gid': 800,
        'groups': None,
        'shell': '/bin/bash',
    },
]

# Initialize directories
DIRS = [
    {
        'path': '/home/appbooster/host',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appbooster',
        'git_install': 'https://github.com/purdue-cs490/appbooster.git',
    },
]
