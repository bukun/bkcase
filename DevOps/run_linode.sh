#!/usr/bin/env bash
# Python 2.7 下运行

fab -f linode_bk.py update

fab -f linode_su.py restart
fab -f linode_bk.py backup
