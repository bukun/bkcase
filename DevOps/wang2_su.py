#!/usr/bin/env python
# encoding: utf-8

from fabric.api import run, env
from helper import update_sys

from cfg import wang2_cfg

env.hosts = ['root@{host}'.format(host=wang2_cfg['host'])]
env.password = wang2_cfg['root_pass']


def restart():
    run('supervisorctl restart all')
