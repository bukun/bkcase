#!/usr/bin/env python
# encoding: utf-8

'''
'''

from fabric.api import cd, run, env
from helper import backup_db, update_proj
from cfg import wang1_cfg, wang1_db_cfg, wang1_proj_cfg

env.hosts = ['{user_name}@{host}'.format(user_name=wang1_cfg['user_name'], host=wang1_cfg['host'])]
env.port = '11022'
env.password = wang1_cfg['user_pass']


def backup():
    for key, val in wang1_db_cfg.items():
        backup_db(key, val)


def update():
    for key, projdic in wang1_proj_cfg.items():
        update_proj(projdic)
