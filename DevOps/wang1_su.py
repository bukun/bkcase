#!/usr/bin/env python
# encoding: utf-8

from fabric.api import run, env
from helper import update_sys

from cfg import wang1_cfg

env.hosts = ['root@{host}'.format(host=wang1_cfg['host'])]
env.password = wang1_cfg['root_pass']


def restart():
    run('supervisorctl restart all')
