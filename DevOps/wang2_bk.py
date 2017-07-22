#!/usr/bin/env python
# encoding: utf-8

'''
'''

from fabric.api import cd, run, env
from helper import backup_db, update_proj
from cfg import wang2_cfg, wang2_db_cfg, wang2_proj_cfg

env.hosts = ['{user_name}@{host}'.format(user_name=wang2_cfg['user_name'], host=wang2_cfg['host'])]
env.password = wang2_cfg['user_pass']


def backup():
    for key, val in wang2_db_cfg.items():
        backup_db(key, val)


def update():
    for key, projdic in wang2_proj_cfg.items():
        update_proj(projdic)
