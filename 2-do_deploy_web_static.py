#!/usr/bin/python3
'''Module Deploy Archive'''

from fabric.api import *
from datetime import datetime

env.hosts = ['35.190.162.122', '35.237.116.99']

@task
def do_deploy(archive_path):
    '''a Fabric script that distributes an archive to your web servers'''
    if (! archive_path):
        return (False)
