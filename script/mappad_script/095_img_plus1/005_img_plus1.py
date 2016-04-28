# -*- coding:cp936 -*-
__author__ = 'bukun'
import os, sys
from PIL import Image

inws = r'D:\w\maplet\MapPicDir\china_zrdl_01\02_zrdl_01'
outws = inws + 'plus'
if os.path.exists(outws):
    pass
else:
    os.mkdir(outws)


def doit(filename):
    in_jpg = os.path.join(inws, filename)
    out_jpg = os.path.join(outws, filename)
    if os.path.exists(out_jpg):
        return True
    im = Image.open(in_jpg)

    out = im.point(lambda i: i + 1 if i == 0 else i)
    out.save(out_jpg)


for wroot, wdirs, wfiles in os.walk(inws):
    for wfile in wfiles:
        if wfile.lower().endswith('.jpg') or wfile.lower().endswith('.gif') or wfile.lower().endswith('.png'):
            print(wfile)
            doit(wfile)
