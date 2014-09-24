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
        'shell': '/bin/false',
    },
]
