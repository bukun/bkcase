# -*- coding:utf-8 -*-
__author__ = 'bukun'

import os
import sys


tmpl = '''INSERT INTO `tabapp` (`uid`, `title`, `keywords`, `desc`, `industry`, `date`, `run_count`, `view_count`, `run_time`, `update_time`, `create_time`, `type`, `html_path`, `cnt_md`, `cnt_html`, `memo`, `lat`, `lon`, `zoom_max`, `zoom_min`, `zoom_current`) VALUES ('{0}', '新增地图标题', ' ', ' ', ' ', '0000-00-00 00:00:00', '0', '0', '0', '0', '0', '0', '0', ' ', ' ', ' ', '40', '105', '7', '4', '4');
'''

current_maps = []

with open('current.txt') as fi:
    cnts = fi.readlines()
for cnt in cnts:
    current_maps.append(cnt.strip())

all_maps = []
for wroot, wdirs, wfiles in os.walk(r'E:\opt\mapws\maplet\00_China_png'):
# for wroot, wdirs, wfiles in os.walk(r'e:\opt\mapws\maplet\00_China_png'):
    for wfile in wfiles:
        if wfile.endswith('.png'):
            mark = False
            for cur_map in current_maps:
                if cur_map in wfile:
                    mark = True
                    break
            if mark:
                continue
            all_maps.append(os.path.splitext(wfile)[0])

print(all_maps)

with open( 'out.sql', 'w') as fo:
    for map_id in all_maps:
        ss = tmpl.format(map_id)
        fo.write(ss)

with open('new.txt','w') as fo:
    for map_id in all_maps:
        fo.write('http://www.maplet.org/map/{0}\r'.format(map_id))