#!/usr/bin/python3
""" Fabric script that distributes an archive to web servers"""
from fabric.api import *
from os import path

env.hosts = ['100.26.178.116', '54.144.154.1']


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
        run("rm -f /data/web_static/current")

        run("""
        ln -s /data/web_static/releases/{}/ /data/web_static/current
        """.format(file_base))

        print("New vision deployed")

        return True
    except Exception:
        return False
