#!/usr/bin/env python
# encoding: utf-8

'''
'''

from fabric.api import cd, run, env
from helper import backup_db, update_proj
from cfg import aliyun2_cfg, aliyun2_db_cfg, aliyun2_proj_cfg

env.hosts = ['{user_name}@{host}'.format(user_name=aliyun2_cfg['user_name'], host=aliyun2_cfg['host'])]
env.password = aliyun2_cfg['user_pass']


def backup():
    for key, val in aliyun2_db_cfg.items():
        backup_db(key, val)


def git_clone():
    with cd('~/deploy'):
        run('git clone https://git.coding.net/osgeo/fangzai.git')
    with cd('~/deploy/fangzai'):
        run('git clone https://github.com/bukun/torcms_helper.git')


def update():
    with cd('~/deploy/TorCMS'):
        run('git pull')

    for key, projdic in aliyun2_proj_cfg.items():
        update_proj(projdic)
