#!/usr/bin/env bash
# a Fabric script that generates a .tgz archive

from fabric.api import sudo, run, hosts, env, local
import datetime

def do_pack():
local("mkdir ./versions")

    try:
        name="web_static_'+%Y-%m-%dT%H:%M:%S'"
        local("tar -zcvf $name.tar.gz ./web_static")
        result = local("mv $name.tar.gz ./versions")
        return(result)
    except:
        return(None)
