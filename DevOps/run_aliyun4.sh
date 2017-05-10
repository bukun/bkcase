#!/usr/bin/env bash
# Python 2.7 下运行


fab -f aliyun4_bk.py update
fab -f aliyun4_su.py restart
fab -f aliyun4_bk.py backup
