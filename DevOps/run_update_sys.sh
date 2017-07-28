#!/usr/bin/env bash
# Python 2.7 下运行


fab -f aliyun1_su.py  update_sys
fab -f aliyun2_su.py  update_sys
fab -f aliyun3_su.py  update_sys

fab -f linode_su.py  update_sys
fab -f wang1_su.py  update_sys
fab -f wang2_su.py  update_sys

