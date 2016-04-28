# -*- coding:cp936 -*-
import os
import random

def get_uu4d():
    sel_arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    slice = random.sample(sel_arr, 4)
    return (''.join(slice))


def get_sig_arr(inws):
    '''
    得到所有的地图的sig列表
    '''
    now_arr = []
    for wroot, wdirs, wfiles in os.walk(inws):
        for wfile in wfiles:
            # hou_lower = os.path.splitext(wfile)[1].lower()
            (qian, hou) = os.path.splitext(wfile)
            if hou.lower() in ['.jpg', '.bmp', '.tif', '.png']:

                # print(qian)
                sig_arr = qian.split('_')
                if len(sig_arr) > 1:

                    sig = sig_arr[-1]
                    if len(sig) == 5 and sig[0] == 's':
                        now_arr.append(sig[1:])
                    else:
                        continue
                else:
                    continue
    return now_arr