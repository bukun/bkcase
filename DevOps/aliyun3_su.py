#!/usr/bin/env python
# encoding: utf-8

from fabric.api import run, env
from cfg import aliyun3_cfg
from helper import update_sys

env.hosts = ['root@{host}'.format(host=aliyun3_cfg['host'])]
env.password = aliyun3_cfg['root_pass']


def update_maplet():
    run('cp /opt/mapdisk/mapws/wcs_maplet/mapproxy.yaml  /home/bk/wcs_maplet/')


def update():
    run('supervisorctl restart all')
