#!/usr/bin/env bash
# Python 2.7 下运行


fab -f wang1_bk.py update
fab -f wang1_su.py restart
fab -f wang1_bk.py backup
