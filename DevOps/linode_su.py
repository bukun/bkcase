#!/usr/bin/env python
# encoding: utf-8

from fabric.api import run, env
from cfg import linode_cfg
from helper import update_sys

env.hosts = ['root@{host}'.format(host=linode_cfg['host'])]
env.password = linode_cfg['root_pass']


def restart():
    run('supervisorctl reload')
    run('supervisorctl restart maplet1')
    run('supervisorctl restart maplet2')
    # run('supervisorctl restart huatu')
