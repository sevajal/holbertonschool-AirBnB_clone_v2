#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents of the web_static folder
of the AirBnB Clone repo, using the function do_pack.'''
from fabric.api import local
import time

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
