# -*- coding:cp936 -*-

# 对拼接的图像进行切分，然后再拼接
#
import os
import sys







def do_with_dir(inws):
    print(inws)
    zz_tif = os.path.split(inws)[1] + '.tif'
    zz_tif_path = os.path.join(inws, zz_tif)
    # if os.path.exists(zz_tif_path):
    #     pass
    # else:
    #     print(inws)




if __name__ == '__main__':
    inws = r'e:\maplet_dvk\MapPicDir'
    for wroot, wdirs, wfiles in os.walk(inws):
        for wdir in wdirs:
            pp_arr = wdir.split('_')
            if len(pp_arr) > 1 and len(pp_arr[-1]) == 5 and pp_arr[-1][0] == 's':
                do_with_dir(os.path.join(wroot, wdir))