#!/usr/bin/env python
# encoding: utf-8

from fabric.api import run, env

from cfg import aliyun3_cfg

env.hosts = ['{user_name}@{host}'.format(user_name=aliyun3_cfg['user_name'], host=aliyun3_cfg['host'])]
env.port = '11022'
env.password = aliyun3_cfg['user_pass']


def update_maplet():
    run('cp /opt/mapdisk/mapws/wcs_maplet/mapproxy.yaml  /home/bk/wcs_maplet/')


def update():
    update_maplet()
