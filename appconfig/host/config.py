# List of packages to be installed
PACKAGES = [
    'vim',
    'git',
    'nginx',
    'docker.io'
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
