# List of packages to be installed
PACKAGES = [
    'build-essential',
    'wget',
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
    'python-requests',
    'uwsgi',
    'uwsgi-plugin-python',
    'gitolite3',
    'redis-server',
    'redis-tools',
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
        'name': 'git',
        'uid': 860,
        'gid': 860,
        'shell': '/bin/bash',
    },
    {
        'name': 'appbooster',
        'uid': 800,
        'gid': 800,
        'groups': ['docker', 'appdcn', 'git'],
        'shell': '/bin/bash',
    },
]

# Initialize directories
DIRS = [
    {
        'path': '/home/appbooster/.ssh',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appbooster',
        'chown_recursive': True,
    },
    {
        'path': '/home/appbooster/host',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appbooster',
        'chown_recursive': True,
        'git_install': 'https://github.com/purdue-cs490/appbooster.git',
    },
    {
        'path': '/home/appbooster/stats',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appbooster',
        'chown_recursive': True,
        'git_install': 'https://github.com/purdue-cs490/appbooster-stats.git'
    },
    {
        'path': '/home/appbooster/logs',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appbooster',
        'chown_recursive': True,
    },
    {
        'path': '/u/controls',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appdcn',
    },
    {
        'path': '/u/apps',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appdcn',
    },
    {
        'path': '/etc/nginx/sites-enabled',
        'perm': 0755,
        'user': 'appbooster',
        'group': 'appbooster',
        'chown_recursive': True,
    },
    {
        'path': '/usr/local/lib/systemd/system',
    },
    {
        'path': '/etc/logstash/conf.d',
        'perm': 0775,
        'user': 'appbooster',
        'group': 'appbooster',
        'chown_recursive': True,
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
        'path': '/etc/nginx/sites-enabled/appbooster-stats',
    },
    {
        'path': '/etc/uwsgi/apps-enabled/appbooster.ini',
    },
    {
        'path': '/home/appbooster/host.ini',
        'user': 'appbooster',
        'group': 'appbooster',
    },
    {
        'path': '/home/appbooster/stats.ini',
        'user': 'appbooster',
        'group': 'appbooster',
    },
    {
        'path': '/home/appbooster/logs/stats_nginx_access',
        'user': 'appbooster',
        'group': 'appbooster',
    },
    {
        'path': '/home/appbooster/logs/stats_nginx_error',
        'user': 'appbooster',
        'group': 'appbooster',
    },
    {
        'path': '/home/appbooster/.ssh/config',
        'user': 'appbooster',
        'group': 'appbooster',
    },
    {
        'path': '/home/git/.gitolite.rc',
        'user': 'git',
        'group': 'git',
        'perm': 0400,
    },
    {
        'path': '/usr/local/lib/systemd/system/docker-autostart.service',
    },
    {
        'path': '/etc/sudoers.d/appbooster-nginx',
        'perm': 0440,
    }
]
