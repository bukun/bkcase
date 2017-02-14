# !/usr/bin/env python
# encoding: utf-8

from fabric.api import cd, run


def update_osgeo():
    pass


def update():
    with cd('~/deploy/TorCMS'):
        run('git pull')
