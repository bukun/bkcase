# -*- coding:cp936 -*-

#
import os
import sys
import arcpy
import maplet_tools


if __name__ == '__main__':
    inws = r'd:\maplet_dvk\MapPicDir'
    now_arr = maplet_tools.get_sig_arr(inws)


    for wroot, wdirs, wfiles in os.walk(inws):
        for wdir in wdirs:
            new_sig = maplet_tools.get_uu4d()
            while new_sig in now_arr:
                new_sig = maplet_tools.get_uu4d()
            if wdir.endswith('_tt'):
                now_arr.append(new_sig)
                raw_path = os.path.join(wroot, wdir)
                new_path = os.path.join(wroot, ''.join([wdir[:-2] , 's' , new_sig]))
                print(raw_path)
                print(new_path)
                os.rename(raw_path, new_path)
    print('For files: ')
    for wroot, wdirs, wfiles in os.walk(inws):
        for wfile in wfiles:
            (qian, hou) = os.path.splitext(wfile)
            new_sig = maplet_tools.get_uu4d()
            while new_sig in now_arr:
                new_sig = maplet_tools.get_uu4d()
            if qian.endswith('_tt'):
                now_arr.append(new_sig)
                raw_path = os.path.join(wroot, wfile)
                new_path = os.path.join(wroot, ''.join([qian[:-2], 's', new_sig, hou.lower()]))
                print(raw_path)
                print(new_path)
                # 这里必须使用arcpy对数据集进行重命名
                arcpy.Rename_management(raw_path, new_path)
                # os.rename(raw_path, new_path)