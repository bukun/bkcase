#!/usr/bin/env python
# encoding: utf-8

from fabric.api import run, env

from cfg import aliyun2_cfg

env.hosts = ['root@{host}'.format(host=aliyun2_cfg['host'])]
env.password = aliyun2_cfg['root_pass']


def restart():
    run('supervisorctl restart drr')
    run('supervisorctl restart yunsuan1')
    run('supervisorctl restart yunsuan2')
