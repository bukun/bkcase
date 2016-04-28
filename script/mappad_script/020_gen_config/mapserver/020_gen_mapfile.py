# -*- coding:utf-8 -*-
# Windows下面

import os
import sys


tmpl = '''
###################################
LAYER
    NAME 'maplet_{0}'
    TYPE raster
    DUMP true
    DATA "{1}.png"
    TEMPLATE 'tpl_{0}'
    PROJECTION
        "init=epsg:3857"
    END
    METADATA
        'ows_title' 'china_3798_0357'
        'wms_title' 'china_3798_0357'
        'ows_srs'  'EPSG:3857'
    END
    STATUS ON
    TRANSPARENCY 100
END
##################################
'''
rst_ws = r'e:\opt\mapws\maplet\00_China_png'
out_mapfile = r'e:\opt\mapws\maplet\maplet_00.map'
with open(out_mapfile, 'w') as fo:

    fo.writelines(open('tmpl_mapfile_0.map').readlines())

    for wroot, wdirs, wfiles in os.walk(rst_ws):

    # pngs = os.listdir(rst_ws)
        for png in wfiles:
            if png.endswith('.png'):
                sig = os.path.splitext(png)[0]
                wpath = wroot[len(rst_ws) + 1:] + '/' +  sig
                print('-' * 20)
                print(sig)
                print(wpath)
                fo.write(tmpl.format( sig, wpath))

    fo.write('\nEND')
