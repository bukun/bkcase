# -*- coding:cp936 -*-

# 对拼接的图像进行切分，然后再拼接
#
import os
import sys
import arcpy


def export_single_part(feapath , outpath, field, prename='', ishp = False):
    '''
    feapath = r'w:\Platform\geodatabase\tools.gdb\tools\bnddb_clip'
    outpath = r'v:'
    prename = 'fd'
    export_single_part(feapath , outpath , prename)
    '''
    # TODO: export attribute .

    field_names = [x.name for x in arcpy.ListFields(feapath)]
    try:
        field_names.remove('OBJECTID')
        field_names.remove('Shape')
        field_names.remove('ID')
        field_names.remove('Shape_Leng')
        field_names.remove('Shape_Length')
        field_names.remove('Shape_Area')
    except:
        pass
    print(field_names)

    arcpy.env.workspace = outpath
    polys = arcpy.SearchCursor(feapath)
    poly = polys.next()


    while poly:
        hao = str((poly.getValue(field)))
        feat = poly.shape
        a = 0

        outfea = prename + hao
        if  ishp :
            outfea  = outfea  + '.shp'
        # print(outfea)
        if arcpy.Exists(outfea):
            arcpy.Delete_management(outfea)
        # clear_feature(os.path.join(outpath, outfea))
        # print('=' * 20)
        # print(outpath)
        # print(outfea)
        # print(feapath)

        arcpy.CreateFeatureclass_management(outpath , outfea, "Polygon", feapath)
        cur = arcpy.InsertCursor(outpath + os.sep + outfea )

        lineArray = arcpy.CreateObject("Array")
        # pntout = gp.CreateObject("Point")

        polyArray = feat.getPart(a)
        pnt = polyArray.next()
        # print('::::::::::::::::::')
        while pnt:

            # print "; " + str(pnt.x) + "; " + str(pnt.y)
            # print(type(pnt))
            # print(pnt)
            lineArray.add(pnt)
            pnt = polyArray.next()
        # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
        feat = cur.newRow()
        # print(lineArray)
        feat.shape = lineArray

        # for fd_name in field_names:
        #     feat.setValue(fd_name, poly.getValue(fd_name))


        cur.insertRow(feat)
        lineArray.removeAll()
        del polyArray
        del pnt
        del feat
        poly = polys.next()


def clear_fea(fea_path):
    if arcpy.Exists(fea_path):
        arcpy.Delete_management(fea_path)
def clear_feas(feas):
    for x in feas:
        if arcpy.Exists(x):
            arcpy.Delete_management(x)




def do_with_dir(inws):
    print(inws)
    zz_tif = os.path.split(inws)[1] + '.tif'

    zz_tif_path = os.path.join(inws, zz_tif)

    if arcpy.Exists(zz_tif_path):
        return

    arcpy.env.workspace = inws

    for wroot, wdirs, wfiles in os.walk(inws):
        for wfile in wfiles:
            hou = os.path.splitext(wfile)[1]
            # print (hou)
            if hou.lower() in ['.png', '.jpg', '.tif', '.bmp']:
                pass
            else:
                continue
            if wfile.startswith('r1'):
                raster1 = os.path.join(inws, wfile)
            elif wfile.startswith('r2'):
                raster2 = os.path.join(inws, wfile)

    print(raster1)
    print(raster2)

    ds1 = arcpy.sa.Raster(raster1)
    ds2 = arcpy.sa.Raster(raster2)


    pix_size1 = int(min(ds1.meanCellWidth, ds1.meanCellHeight) * 0.98)
    pix_size2 = int(min(ds2.meanCellWidth, ds2.meanCellHeight) * 0.98)

    res_res = min(pix_size1, pix_size2)
    res_resample = int(res_res * 0.8)

    infea = os.path.join(inws, 'bnd.shp')
    field = 'img'
    prename = 'xx_'


    mask1_tmp = 'xx_r1.shp'
    mask1 = 'xx_r1_buf.shp'

    mask2_tmp = 'xx_r2.shp'
    mask2 = 'xx_r2_buf.shp'
    clear_fea(mask1_tmp)
    clear_fea(mask2_tmp)

    clear_feas([mask1_tmp, mask1, mask2_tmp, mask2])

    export_single_part(infea, inws, field, prename, ishp=True)

    # arcpy.Buffer_analysis()

    arcpy.Buffer_analysis(mask1_tmp, mask1,  res_resample)


    arcpy.Buffer_analysis(mask2_tmp, mask2,  res_resample)



    re1 = 'xx_re1.tif'
    re2 = 'xx_re2.tif'

    print('resamle')


    clear_feas([re1, re2])

    arcpy.Resample_management(raster1, re1, res_resample, "CUBIC")
    arcpy.Resample_management(raster2, re2, res_resample, "CUBIC")




    #########################
    tmp1 = 'xx_m1.tif'
    tmp2 = 'xxx_m2.tif'

    clear_feas([tmp1, tmp2])

    print('extract')

    outExtractByMask2 = arcpy.sa.ExtractByMask(re2, mask2)
    outExtractByMask2.save(tmp2)

    outExtractByMask1 = arcpy.sa.ExtractByMask(re1, mask1)
    outExtractByMask1.save(tmp1)
    # clear_feas([tmp1, tmp2])


    resultif = 'xx_mosiac.tif'
    clear_fea(resultif)
    print('mosaic')
    arcpy.MosaicToNewRaster_management("{0};{1}".format(tmp1, tmp2),
                                       inws, resultif, '#',
                                       "8_BIT_UNSIGNED", res_resample, "3", "LAST", "FIRST")


    clear_fea(zz_tif)
    arcpy.Resample_management(resultif, zz_tif, res_res, "CUBIC")



    clear_feas([mask1_tmp, mask1, mask2_tmp, mask2, re1, re2, tmp1, tmp2, resultif])

if __name__ == '__main__':
    inws = r'd:\maplet_dvk\MapPicDir\MapPicSig\liaoning1995_dd008dd'
    for wroot, wdirs, wfiles in os.walk(inws):
        for wdir in wdirs:
            pp_arr = wdir.split('_')
            if len(pp_arr) > 1 and len(pp_arr[-1]) == 5 and pp_arr[-1][0] == 's':
                do_with_dir(os.path.join(wroot, wdir))
