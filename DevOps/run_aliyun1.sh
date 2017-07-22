#!/usr/bin/env bash
# Python 2.7 下运行
fab -f aliyun1_bk.py update
fab -f aliyun1_su.py restart

# fab -f aliyun1_bk.py backup