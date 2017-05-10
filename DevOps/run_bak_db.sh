#!/usr/bin/env bash
# Python 2.7 下运行

fab -f aliyun1_bk.py backup
fab -f aliyun2_bk.py backup
fab -f aliyun4_bk.py backup
fab -f linode_bk.py backup

