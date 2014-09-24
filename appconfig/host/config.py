# List of packages to be installed
PACKAGES = [
    'vim',
    'git',
    'nginx',
    'mysql-server-5.5',
    'docker.io',
    'python2.7',
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
        'git_install': 'https://github.com/purdue-cs490/appbooster',
    },
]
