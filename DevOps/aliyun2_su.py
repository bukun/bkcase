#!/usr/bin/env python
# encoding: utf-8

from fabric.api import run, env
from cfg import aliyun2_cfg
from helper import update_sys

env.hosts = ['root@{host}'.format(host=aliyun2_cfg['host'])]
env.password = aliyun2_cfg['root_pass']


def restart():
    # run('supervisorctl restart drr1')
    # run('supervisorctl restart drr2')
    run('supervisorctl restart yunsuan1')
    run('supervisorctl restart yunsuan2')
    run('supervisorctl restart gislab')
