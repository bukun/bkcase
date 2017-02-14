#!/usr/bin/env bash
# Python 2.7 下运行


fab -f aliyun2_bk.py update
fab -f aliyun2_su.py restart
fab -f aliyun2_bk.py backup