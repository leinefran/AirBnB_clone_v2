#!/usr/bin/env bash
'''Module Compress File'''

from fabric.api import *
from datetime import datetime


def do_pack():
    '''a Fabric script that generates a .tgz archive'''
    local("mkdir -p ./versions")

    try:
        name = "web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
        local("tar -zcvf " + name + " ./web_static")
        result = local("mv " + name + " ./versions")
        return(result)
    except:
        return(None)
