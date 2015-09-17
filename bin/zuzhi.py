# -*- coding: utf-8 -*-
import os
import sys

'''

'''

fz_dict = {'part':'ch', 'ch':'sec', 'sec': 'sub' }
# magic_str = '%----%'
magic_str = '%%%% ==== %%%% ==== %%%% ==== %%%%'


def zuzhi_dir(inws,sig_single, w_len):
    sig_zucheng = fz_dict[sig_single]
    print(inws)    
    # 只以文件夹前面进行判断
    # 不对的话，则直接返回

    chfile = ''
    zucheng_files = []
    for wroot, wdirs, wfiles in os.walk(inws):
        for wfile in wfiles:
            if wfile.endswith('tex') == False:
                continue
            if wfile.startswith(sig_single):
                # 找到唯一的chfile
                chfile = os.path.join(wroot, wfile)
            if wfile.startswith(sig_zucheng):
                wfile = os.path.join(wroot, wfile)
                zucheng_files.append(wfile)
    if len(chfile) > 0:
        pass
    else:
        return
    zucheng_files.sort()
    
    cnts = file(chfile).readlines()
    
    fo = open(chfile, 'w')
    for cnt in cnts:
        if cnt.startswith('%----%') or cnt.startswith(magic_str):
            break
        fo.write(cnt)
    fo.write('%s\n' % magic_str)
    for zucheng_file in zucheng_files:
        tep = file(zucheng_file).next()
        fo.write('%% %s' % (tep))
        zucheng_file = '.' + zucheng_file[w_len:-4]
        fo.write('\input{%s}\n\n' % (zucheng_file))

def do_for_dir(inws):
    w_len = len(inws)
    for wroot, wdirs, wfiles in os.walk(inws):
        for wdir in wdirs:
            indir = os.path.join(wroot, wdir)
            fzkeys = fz_dict.keys()
            
            '''
            此处对keys进行遍历，然后逐个判断
            我想这样代码更好理解
            因为也不会太多，不考虑效率的事了
            '''
            for fzkey in fzkeys:
                if wdir.startswith(fzkey):
                    sig_single = fzkey
                    zuzhi_dir(indir, sig_single, w_len)

if __name__ == '__main__':
    inws  = '/home/bk/python_gis2'
    do_for_dir(inws)