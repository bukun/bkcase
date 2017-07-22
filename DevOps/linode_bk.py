#!/usr/bin/env python
# encoding: utf-8

from fabric.api import cd, run, env

from cfg import linode_cfg, linode_db_cfg, linode_proj_cfg

from helper import backup_db, update_proj

env.hosts = ['{user_name}@{host}'.format(user_name=linode_cfg['user_name'], host=linode_cfg['host'])]
env.password = linode_cfg['user_pass']


def backup():
    for key, val in linode_db_cfg.items():
        backup_db(key, val)

def update():
    for key, projdic in linode_proj_cfg.items():
        update_proj(projdic)