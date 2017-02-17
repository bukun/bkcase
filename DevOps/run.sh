#!/usr/bin/env bash
# Python 2.7 下运行
fab -f aliyun1_bk.py update
fab -f aliyun1_su.py restart

fab -f aliyun2_bk.py update
fab -f aliyun2_su.py restart

fab -f aliyun4_bk.py update
fab -f aliyun4_su.py restart


fab -f linode_bk.py update
fab -f linode_su.py restart
