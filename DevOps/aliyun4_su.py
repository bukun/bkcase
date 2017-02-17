#!/usr/bin/env python
# encoding: utf-8

from fabric.api import run, env

from cfg import aliyun4_cfg

env.hosts = ['root@{host}'.format(host=aliyun4_cfg['host'])]
env.password = aliyun4_cfg['root_pass']


def restart():
    run('supervisorctl restart all')
