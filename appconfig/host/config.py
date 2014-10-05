# List of packages to be installed
PACKAGES = [
    'build-essential',
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

# List of groups to be added
GROUPS = [
    # {
    #     'name': 'docker',
    #     'gid': 850,
    # }
]

# List of users to be added
USERS = [
    {
        'name': 'appbooster',
        'uid': 800,
        'gid': 800,
        'groups': ['docker'],
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
    {
        'path': '/u/apps',
        'perm': 01777,
        'user': 'root',
        'group': 'root',
    },
    {
        'path': '/u/apps/logs',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appbooster',
    },
]
