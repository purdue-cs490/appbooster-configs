# List of packages to be installed
PACKAGES = [
    'build-essential',
    'git',
    'python',
    'python-dev',
    'python-pip',
    'python-virtualenv',
    'uwsgi',
    'uwsgi-plugin-python',
]

# List of groups to be added
GROUPS = [
]

# List of users to be added
USERS = [
    {
        'name': 'appdcn',
        'uid': 850,
        'gid': 850,
        'shell': '/bin/false',
    },
    {
        'name': 'appbooster',
        'uid': 800,
        'gid': 800,
        'groups': ['docker', 'appdcn'],
        'shell': '/bin/bash',
    },
]

# Initialize directories
DIRS = [
    {
        'path': '/u/app',
        'perm': 0755,
        'user': 'appdcn',
        'group': 'appdcn',
    },
    {
        'path': '/u/control',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appdcn',
    }
]

FILES = [
    {
        'path': '/etc/uwsgi/apps-enabled/app.ini',
    }
]
