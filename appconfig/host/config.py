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
    'uwsgi-plugin-python',
]

# List of groups to be added
GROUPS = [
    # {
    #     'name': 'docker',
    #     'gid': 900,
    # }
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
        'path': '/home/appbooster/host',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appbooster',
        'git_install': 'https://github.com/purdue-cs490/appbooster.git',
    },
    {
        'path': '/home/appbooster/logs',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appbooster',
    },
]

FILES = [
    {
        'path': '/etc/default/grub',
    },
    {
        'path': '/etc/nginx/sites-enabled/appbooster.com',
    },
    {
        'path': '/etc/uwsgi/apps-enabled/appbooster.ini',
    },
    {
        'path': '/home/appbooster/host.ini',
        'user': 'appbooster',
        'group': 'appbooster',
    },
]
