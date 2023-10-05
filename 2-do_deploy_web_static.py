#!/usr/bin/python3
""" Fabric script that distributes an archive to web servers"""
from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['100.26.178.116', '54.144.154.1']


def do_pack():
    """ script that generates a .tgz archive """
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")

    local("mkdir -p versions")
    archive = "versions/web_static_{}.tgz".format(date_time)

    if local("tar -czvf {} web_static".format(archive)).succeeded:
        return archive
    else:
        return None


def do_deploy(archive_path):
    """
    function distributes an archive to web servers
    """
    if not path.exists(archive_path):
        return False

    try:
        file_name = archive_path.split('/')[-1]
        file_base = file_name.split('.')[0]

        put(archive_path, '/tmp/')

        run("mkdir -p /data/web_static/releases/{}/".format(file_base))

        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            file_name, file_base))

        run("rm /tmp/{}".format(file_name))
        run("""
        mv /data/web_static/releases/{}/web_static/* 
        /data/web_static/releases/releases/{}/""".format(file_base, file_base))
        run("rm -rf /data/web_static/releases/{}/web_static".format(file_base))
        run("rm -rf /data/web_static/current")

        run("""
        ln -s /data/web_static/releases/{}/ /data/web_static/current
        """.format(file_base))

        print("New vision deployed")

        return True
    except Exception:
        return False
