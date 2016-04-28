# -*- coding:utf-8 -*-
# Windows下面执行

__author__ = 'bukun'
import os
import sys
import yaml

mapserver_ip = '121.42.29.253'
mapserver_ip = '159.226.123.26'

out_yaml_file = r'D:\opt\mapws\wcs_maplet\seed.yaml'
uu = yaml.load(open('seed.yaml'))

for key in uu.keys():
    print(key)

rst_ws = r'D:\opt\mapws\maplet\00_China_png'
pngs = os.listdir(rst_ws)
for png in pngs:
    if png.endswith('.png'):
        sig = 'maplet_' + os.path.splitext(png)[0]
        # fo.write(tmpl.format('maplet_' + sig))
        uu['seeds'][sig] = {}
        uu['seeds'][sig]['caches'] = [sig]
        uu['seeds'][sig]['levels'] = {}
        uu['seeds'][sig]['levels']['to']  = 8
        uu['seeds'][sig]['levels']['from']  = 4
        uu['seeds'][sig]['refresh_before'] = {}
        uu['seeds'][sig]['refresh_before']['time'] = '2013-10-10T12:35:00'



        # new_dic = {'name': sig,'title': sig, 'sources': [sig]}
        # uu['layers'].append(new_dic)



fo = open(out_yaml_file, 'w')
yaml.dump(uu, fo)


