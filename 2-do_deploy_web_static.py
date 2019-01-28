#!/usr/bin/python3
'''Module Deploy Archive'''

from fabric.api import *
from datetime import datetime

env.key_filename = "~/.ssh/holberton"
env.hosts = ['35.190.162.122', '35.237.116.99']
env.user = 'ubuntu'
env.password = "betty"

@task
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

@task
def do_deploy(archive_path):
    '''a Fabric script that distributes an archive to your web servers'''
    if not archive_path:
        return (False)

    # using the 'split' method to extract only the file name w/o the extension;
    # 'web_static_20170315003959'
    filename = archive_path.split("/")[1][:-4]

    try:
        # upload tar archive:
        upload = put(archive_path, "/tmp/")

        # Verify the upload:
        upload.succeeded

        # Extract the contents of a tar archive:
        content = run("tar xzvf" + filename + ".tgz")

        # Move contents to a different folder:
        cd("/tmp/")
        file_path = run("mv " + content + " /data/web_static/releases/"

        # Delete the archive:
        run("rm -rf /tmp/" + filename + ".tgz")

        # Delete a symbolic link:
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link:
        run("ln -sf " + file_path + " /data/web_static/current")

        print("It worked!")
        return (True)

    except:
        print("Fail")
        return (False)
