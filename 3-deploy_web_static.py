#!/usr/bin/python3
'''Fabric script that creates and distributes an archive to my web servers,
using the function deploy.'''
from fabric.api import env, local, put, run
import os
import time

env.hosts = ['web-01.sevajal.tech', 'web-02.sevajal.tech']
env.user = 'ubuntu'
env.key = '~/.ssh/school'


def do_pack():
    '''pack the files in the folder'''
    timestr = time.strftime("%Y%m%d%H%M%S")
    file = "web_static_" + timestr + ".tgz"
    try:
        local('mkdir -p versions')
        local('tar -cvzf versions/{} web_static'.format(file))
        return ('versions/{}'.format(file))
    except Exception as error:
        return (None)


def do_deploy(archive_path):
    '''Deploy the archive in the web servers'''
    if not os.path.exists(archive_path):
        return (False)
    file = archive_path.split('/')[1]
    name = file.split('.')[0]
    try:
        put(archive_path, '/tmp/{}'.format(file))
        run('mkdir -p /data/web_static/releases/{}/'.format(name))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
            .format(file, name))
        run('rm /tmp/{}'.format(file))
        run('mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}/'.format(name, name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(name))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(name))
        return (True)
    except Exception as error:
        return (False)


def deploy():
    '''Creates and deploy an archive to the web servers'''
    archive_path = do_pack()
    if not archive_path:
        return (False)
    return (do_deploy(archive_path))
