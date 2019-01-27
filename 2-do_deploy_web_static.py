#!/usr/bin/python3
'''Module Deploy Archive'''

from fabric.api import *
from datetime import datetime


env.hosts = ['35.190.162.122', '35.237.116.99']
env.user = 'ubuntu'
env.password = "betty"


@task
def do_deploy(archive_path):
    '''a Fabric script that distributes an archive to your web servers'''
    if (! archive_path):
        return (False)

    # upload a tar archive:
    with cd("/tmp"):
        upload = put("/home/vagrant/Holberton/AirBnB_clone_v2/versions/" +
                     "web_static_20190127003308.tgz")

    # Verify the upload:
    upload.succeeded

    # Extract the contents of a tar archive:
    content = run("tar xzvf /tmp/web_static_20190127003308.tgz")

    # Move contents to a different folder:
    run("mv" + content + "/data/web_static/releases/web_static_20190127003308")

    # Delete the archive:
    run("rm /tmp/web_static_20190127003308.tgz")

    # Delete a symbolic link:
    run("rm /data/web_static/current")

    # Create a new symbolic link:
    file_path = "/data/web_static/releases/web_static_20190127003308"
    run("ln -sf" + file_path + "/data/web_static/current")
