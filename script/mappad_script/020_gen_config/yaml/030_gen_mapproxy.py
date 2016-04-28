# -*- coding:utf-8 -*-
# Windows下面执行

__author__ = 'bukun'
import os
import sys
import yaml


def do_for_raster(mapserver_ip, mapfile_ws, out_yaml_file):
    uu = yaml.load(open('mapproxy.yaml'))
    rst_ws = r'e:\opt\mapws\maplet\00_China_png'
    pngs = os.listdir(rst_ws)
    for wroot, wdirs, wfiles in os.walk(rst_ws):
        for png in wfiles:
        # for png in pngs:
            if png.endswith('.png'):
                pass
            else:
                continue
            sig = 'maplet_' + os.path.splitext(png)[0]
            # fo.write(tmpl.format('maplet_' + sig))
            uu['sources'][sig] = {}
            uu['sources'][sig]['type'] = 'wms'
            uu['sources'][sig]['image'] = {'transparent_color_tolerance': 0, 'transparent_color': '#000000'}

            uu['sources'][sig]['req'] = {}
            uu['sources'][sig]['req']['url'] = 'http://{0}/cgi-bin/mapserv?map={1}/maplet/maplet_00.map'.format(
                mapserver_ip, mapfile_ws)
            uu['sources'][sig]['req']['layers'] = sig

            uu['caches'][sig] = {}
            uu['caches'][sig]['grids'] = ['webmercator']
            uu['caches'][sig]['grids'] = ['webmercator']
            uu['caches'][sig]['sources'] = [sig]

            new_dic = {'name': sig, 'title': sig, 'sources': [sig]}
            uu['layers'].append(new_dic)

    with  open(out_yaml_file, 'w') as fo:
        yaml.dump(uu, fo)

def do_for_list(mapserver_ip, mapfile_ws, out_yaml_file):
    all_list = ['9000']
    uu = yaml.load(open(out_yaml_file))
    for sig in all_list:
        sig = 'maplet_' + sig
        # fo.write(tmpl.format('maplet_' + sig))
        uu['sources'][sig] = {}
        uu['sources'][sig]['type'] = 'wms'
        uu['sources'][sig]['image'] = {'transparent_color_tolerance': 0, 'transparent_color': '#000000'}

        uu['sources'][sig]['req'] = {}
        uu['sources'][sig]['req']['url'] = 'http://{0}/cgi-bin/mapserv?map={1}/maplet/maplet_00.map'.format(
            mapserver_ip, mapfile_ws)
        uu['sources'][sig]['req']['layers'] = sig

        uu['caches'][sig] = {}
        uu['caches'][sig]['grids'] = ['webmercator']
        uu['caches'][sig]['sources'] = [sig]

        new_dic = {'name': sig, 'title': sig, 'sources': [sig]}
        uu['layers'].append(new_dic)

    with  open(out_yaml_file, 'w') as fo:
        yaml.dump(uu, fo)
def gen_by_ip(mapserver_ip, mapfile_ws, out_yaml_file):
    do_for_raster(mapserver_ip, mapfile_ws, out_yaml_file)
    do_for_list(mapserver_ip, mapfile_ws, out_yaml_file)


if __name__ == '__main__':
    mapserver_ip = '121.42.29.253'

    # mapserver_ip = '159.226.123.26'
    out_yaml_file = r'e:\opt\mapws\wcs_maplet\mapproxy.yaml'
    mapfile_ws = '/opt/mapdisk/mapws'
    gen_by_ip(mapserver_ip, mapfile_ws, out_yaml_file)


