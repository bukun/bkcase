#!/usr/bin/env python
# encoding: utf-8

'''
'''

from fabric.api import cd, run, env
from helper import backup_db, update_proj
from cfg import aliyun4_cfg, aliyun4_db_cfg, aliyun4_proj_cfg

env.hosts = ['{user_name}@{host}'.format(user_name=aliyun4_cfg['user_name'], host=aliyun4_cfg['host'])]
env.password = aliyun4_cfg['user_pass']


def backup():
    for key, val in aliyun4_db_cfg.items():
        backup_db(key, val)


def update():
    with cd('~/deploy/TorCMS'):
        run('git pull')

    for key, projdic in aliyun4_proj_cfg.items():
        update_proj(projdic)
