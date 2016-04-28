# -*- coding:utf-8 -*-
import arcpy
import os



if __name__ == '__main__':
    infea = r'd:\shihang\gdbws\demo_3857.gdb\region\xian201210'
    outpath = r'd:\shihang\gdbws\demo_3857.gdb\region'
    field= 'name_pinyin'
    prename = 'xian'
    export_single_part(infea, outpath, field, prename, ishp=False)
