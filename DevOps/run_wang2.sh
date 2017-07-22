#!/usr/bin/env bash
# Python 2.7 下运行


fab -f wang2_bk.py update
fab -f wang2_su.py restart
fab -f wang2_bk.py backup
