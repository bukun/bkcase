# -*- coding:cp936 -*-
'''
找到原始目录中重复的

输入文件名的确定：
上层文件夹， xxx_20
当前文件名, 146_xxx，146转16进制，为92。
两字符串连接：
2092，，即为文件名。
'''
import os
import sys
from maplet_tools import get_sig_arr

inws = r'd:\maplet_dvk\MapPicDir'

all_arr = get_sig_arr(inws)


def finddupl(lst):
    """找出 lst 中有重复的项
        (与重复次数无关，且与重复位置无关)
    """
    exists, dupl = set(), set()
    for item in lst:
        if item in exists:
            dupl.add(item)
        else:
            exists.add(item)
    return dupl


print('Result ----')
print(finddupl(all_arr))
