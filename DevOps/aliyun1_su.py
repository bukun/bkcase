#!/usr/bin/env python
# encoding: utf-8

from fabric.api import run, env
from cfg import aliyun1_cfg
from helper import update_sys

env.hosts = ['root@{host}'.format(host=aliyun1_cfg['host'])]
env.password = aliyun1_cfg['root_pass']


def restart():
    run('supervisorctl restart osgeo1')
    run('supervisorctl restart osgeo2')
    run('supervisorctl restart geodata')
    run('supervisorctl restart wds')
    run('supervisorctl restart wetland')

