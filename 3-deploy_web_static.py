#!/usr/bin/python3
'''Fabric script that creates and distributes an archive to my web servers,
using the function deploy.'''
from fabric.api import env
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ['web-01.sevajal.tech', 'web-02.sevajal.tech']
env.user = 'ubuntu'
env.key = '~/.ssh/school'


def deploy():
    '''Creates and deploy an archive to the web servers'''
    try:
        archive_path = do_pack()
    except Exception as error:
        return (False)
    return (do_deploy(archive_path))
