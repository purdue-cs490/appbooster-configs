from __future__ import print_function

import os

import apt
import files
import user
import command

from config import *


def print_green(s):
    print('\033[32m' + s + '\033[0m')


def print_red(s):
    print('\033[31;1m' + s + '\033[0m')


def install():
    if not os.geteuid() == 0:
        print_red("Must be run as root")
        return 2

    try:
        print_green("Installing packages...")
        apt.update()
        apt.upgrade()
        apt.install(PACKAGES)

        print_green("Adding users and groups...")
        user.add_groups(GROUPS)
        user.add_users(USERS)

        print_green("Installing directories...")
        files.install_dirs(DIRS)

        print_green("Installing files...")
        files.install_files(FILES)

        print_green("Updating grub configs...")
        command.run('update-grub')

        print_green("Setting up MySQL...")
        command.run_sudo_script("""
            mysql -e "CREATE USER 'appbooster'@'localhost' IDENTIFIED BY 'appbooster';
            CREATE DATABASE appdb;
            GRANT ALL PRIVILEGES ON appdb.* TO 'appbooster'@'localhost';"
            """, check=False)

        print_green("Setting up Git server...")
        command.run_sudo_script("""
            set -e
            if [ ! -f ~/.ssh/appbooster ]; then
                ssh-keygen -q -f /home/appbooster/.ssh/appbooster -N ""
            fi
            git config --global user.name "appbooster"
            git config --global user.email "appbooster@localhost"
            """, user='appbooster')
        command.run_sudo_script("""
            set -e
            if [ ! -d /home/git/repositories/gitolite-admin.git ]; then
                cd ~
                gitolite setup -pk /home/appbooster/.ssh/appbooster.pub
            fi
            """, user='git')

        print_green("Setting up appbooster host...")
        command.run_sudo_script("""
            set -e
            cd /home/appbooster/host
            virtualenv --no-site-packages ENV
            source ENV/bin/activate
            pip install -r requirements.txt
            export ENVIRONMENT=prod
            ./manage.py migrate
            deactivate
            """, user='appbooster')
        command.run_sudo_script("""
            mkdir -p ~/local/VREF
            ln -sf /home/appbooster/host/scripts/update ~/local/VREF/deploy
            """, user='git')

        print_green("Setting up appbooster stats...")
        command.run_sudo_script("""
            set -e
            cd /home/appbooster/stats
            virtualenv --no-site-packages ENV
            source ENV/bin/activate
            pip install -r requirements.txt
            deactivate
            """, user='appbooster')

        print_green("Restarting services...")
        command.run_sudo_script("""
            sudo rm -f /etc/nginx/site-enabled/default
            """)
        command.run_script("""
            systemctl reload uwsgi
            systemctl reload nginx
            """)

        print_green("Enabling systemd services...")
        command.run_script("""
            systemctl daemon-reload
            systemctl enable docker-autostart.service
            """)

        print_green("Installing elasticsearch and logstash...")
        command.run_script("""
            ES_DEB_REPO="deb http://packages.elasticsearch.org/elasticsearch/1.4/debian stable main"
            LS_DEB_REPO="deb http://packages.elasticsearch.org/logstash/1.4/debian stable main"
            wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -
            if ! grep -Fxq "$ES_DEB_REPO" /etc/apt/sources.list; then
                echo "$ES_DEB_REPO" >> /etc/apt/sources.list
            fi
            if ! grep -Fxq "$LS_DEB_REPO" /etc/apt/sources.list; then
                echo "$LS_DEB_REPO" >> /etc/apt/sources.list
            fi
            apt-get update
            apt-get -y install logstash elasticsearch
            """)

        print_green("Succeed!")
    except KeyboardInterrupt:
        pass
    except Exception:
        print_red("Error:")
        raise
