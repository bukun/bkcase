#!/usr/bin/env python
# encoding: utf-8
'''

'''

from fabric.api import cd, run, env
from cfg import aliyun1_cfg, aliyun1_db_cfg, aliyun1_proj_cfg
from helper import backup_db, update_proj

env.hosts = ['{user_name}@{host}'.format(user_name=aliyun1_cfg['user_name'], host=aliyun1_cfg['host'])]
env.password = aliyun1_cfg['user_pass']


def backup():
    for key, val in aliyun1_db_cfg.items():
        backup_db(key, val)


def update():
    with cd('~/deploy/TorCMS'):
        run('git pull')

    for key, projdic in aliyun1_proj_cfg.items():
        update_proj(projdic)
