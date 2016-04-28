# -*- coding: cp936 -*-
'''
替代原来的。
sig直接写到文件中，这样设计更简洁。

Windows下运行
'''
import os
import sys
import arcpy
import yaml
import shutil

def build_path(outws):
    if os.path.exists(outws):
        pass
    else:
        os.mkdir(outws)    
proj3857 = r'D:\maplet_dvk\tools\EPSG3857.prj'
inws = r'D:\maplet_dvk\MapPicDir'
# inws = r'd:\maplet_dvk\MapPicDir\raw\中华人民共和国行政区划沿革地图集\204'

outws = r'd:\maplet_dvk\MapPicDir_png'
tmp_directory = r'd:\maplet_dvk\MapPicDir_tmp'
publish_ws = r'D:\opt\mapws\maplet\00_China_png'

build_path(outws)
build_path(tmp_directory)
build_path(publish_ws)
arcpy.env.workspace = tmp_directory


# 正式发布的文件


def abs_rm_dir(Dir):
    shutil.rmtree(Dir)
    os.mkdir(Dir)

def get_published_sigs(publish_ws):
    out_arr = []
    for wroot, wdirs, wfiles in os.walk(publish_ws):
        for wfile in wfiles:
            if wfile.endswith('.png'):
                out_arr.append(wfile[:4])
    return out_arr

published_sig_arr = get_published_sigs(publish_ws)

def is_exists(filename):
    '''
    判断输出文件夹与发布文件平面是否已经有，
    如果有，则跳过。
    不然，生成png文件。
    '''
    test_file = os.path.join(publish_ws, filename)
    if os.path.exists(test_file):
        return True
    test_file2 = os.path.join(outws, filename)
    if os.path.exists(test_file2):
        return True
    return False


def clear_fea(in_fea):
    if arcpy.Exists(in_fea):
        arcpy.Delete_management(in_fea)


if os.path.exists(outws):
    pass
else:
    os.mkdir(outws)

def get_pix_size(yaml_file):
    pix_size = None
    if os.path.exists(yaml_file):
        f = open(yaml_file)

        # 导入
        yaml_dic = yaml.load(f)

        if 'cell_size' in yaml_dic.keys():
            pix_size = yaml_dic['cell_size']
    return pix_size

def do_with_shp(raw_raster, raw_shp, out_raster, pix_size):
    in_shp = 'xx_in_shp_densi.shp'
    clear_fea(in_shp)
    arcpy.Copy_management(raw_shp, in_shp)
    arcpy.Densify_edit(in_shp, "DISTANCE", "20000")
    print('with shpape :')
    in_raster = 'xx_remaple_twice.tif'
    clear_fea(in_raster)
    print(' ' * 4 + 'resample ... ')
    arcpy.Resample_management(raw_raster, in_raster, int(pix_size * 0.9 ), "CUBIC")
    tmp_raster = 'xx_with_extract.tif'
    tmp_raster2 = 'xx_with_project.tif'
    in_shp_buf = 'xx_shp_buf.shp'
    clear_fea(in_shp_buf)
    arcpy.Buffer_analysis(in_shp, in_shp_buf, pix_size)
    in_shp_proj = 'xx_shp_proj.shp'
    clear_fea(in_shp_proj)
    arcpy.Project_management(in_shp, in_shp_proj, proj3857, '', arcpy.Describe(in_raster).spatialReference)

    clear_fea(tmp_raster)
    clear_fea(tmp_raster2)

    print(' ' * 4 + 'extract ... ')
    outExtractByMask2 = arcpy.sa.ExtractByMask(in_raster, in_shp_buf)
    outExtractByMask2.save(tmp_raster)
    try:
        print('-' * 20)
        print('    to project ...')
        print(tmp_raster)
        print(out_raster)

        arcpy.ProjectRaster_management(tmp_raster, tmp_raster2, proj3857, 'CUBIC', pix_size)
        # clear_fea(tmp_raster)
    except:
        print "Project Raster example failed."
        print arcpy.GetMessages()
    print(' ' * 4 + 'extract ... ')
    outma8 = arcpy.sa.ExtractByMask(tmp_raster2, in_shp_proj)
    outma8.save(out_raster)

def tif_to_png(tifile, pngfile):
    print('to png file.')
    clear_fea(output_result_png)
    arcpy.CopyRaster_management(tifile, pngfile,
                                '',  # config_keyword
                                '',  # background_value
                                '',  # nodata_value
                                '',  # onebit_to_eightbit
                                'ColormapToRGB',  # colormap_to_RGB
                                '8_BIT_UNSIGNED',  # pixel_type
                                )

def get_directory_sig(path_root):
    tmp_tt = path_root.split('dd')
    for x in tmp_tt:
        if len(x) == 3:
            return 'd{0}'.format(x)
    return 'dfff'

for wroot, wdirs, wfiles in os.walk(inws):
    for wfile in wfiles:
        # hou_lower = os.path.splitext(wfile)[1].lower()
        (qian, hou) = os.path.splitext(wfile)
        if hou.lower() in ['.jpg', '.bmp', '.tif', '.png']:
            print('=' * 40)
            abs_rm_dir(tmp_directory)
            in_raster1 = os.path.join(wroot, wfile)

            print(in_raster1)
            # print(qian)
            sig_arr = qian.split('_')
            if len(sig_arr) > 1:
                sig = sig_arr[-1]
                if len(sig) == 5 and sig[0] == 's':
                    # print('Do with it ... ')
                    pass
                else:
                    continue
            else:
                continue

            # 是否已经发布
            if sig[1:] in published_sig_arr:
                #  pass
                # print('has benn published.')
                continue


            print('infile {0}'.format(wfile))
            dd_out_dir_sig = get_directory_sig(wroot)

            dd_out_path = os.path.join(outws, dd_out_dir_sig)
            if os.path.exists(dd_out_path):
                pass
            else:
                os.mkdir(dd_out_path)
            output_result_png = os.path.join(dd_out_path, sig[1:] + '.png')


            # 是否当前已经存在
            if arcpy.Exists(output_result_png):
                # print('Esists: ... ')
                continue


            pix_size = get_pix_size( os.path.join(wroot, qian + '.yaml') )


            desc_in_raster = arcpy.sa.Raster(in_raster1)
            if pix_size:
                pass
            else:
                pix_size = int(min(desc_in_raster.meanCellWidth, desc_in_raster.meanCellHeight) * 0.98)

            in_raster_sr = desc_in_raster.spatialReference
            # print(pix_size)

            # pix_size = 1000
            if pix_size < 5:
                continue



            out_result_tif = 'xx_result' + sig[1:] + '.tif'

            clear_fea(out_result_tif)

            in_shp = os.path.join(wroot, os.path.splitext(wfile)[0] + '.shp')
            bnd_shp = os.path.join(wroot, 'bnd.shp')
            if os.path.exists(bnd_shp) and arcpy.Describe(bnd_shp).shapeType == 'Polygon':
                do_with_shp(in_raster1, bnd_shp, out_result_tif, pix_size)

            elif os.path.exists(in_shp) and arcpy.Describe(in_shp).shapeType == 'Polygon':
                do_with_shp(in_raster1, in_shp, out_result_tif, pix_size)

            else:
                print('project ... ')

                arcpy.ProjectRaster_management(in_raster1, out_result_tif, proj3857, 'CUBIC', pix_size)

                # print "Project Raster example failed."
                #     print arcpy.GetMessages()


            tif_to_png(out_result_tif, output_result_png)

            clear_fea(out_result_tif)
