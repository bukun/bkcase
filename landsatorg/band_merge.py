# -*- coding:utf-8 -*-
import os
import sys
import glob
TMP_DIR = '/home/bk/v'

def in_db(file1):
    dh = ['11327', '11327', '11328', \
          '11427', '11428', '11429', \
          '11527', '11528', '11529', '11530', '11531', \
          '11626', '11627', '11628', '11629', '11630', '11631', \
          '11726', '11727', '11728', '11729', '11730', '11731', '11732', \
          '11825', '11826', '11827', '11828', '11829', '11830', '11831', '11832', \
          '11924', '11925', '11926', '11927', '11928', \
          '11929', '11930', '11931', '11932', '11933', \
          '12023', '12024', '12025', '12026', '12027', \
          '12028', '12029', '12030', '12031', '12032', '12033', \
          '12123', '12124', '12125', '12126', '12127', \
          '12128', '12129', '12130', '12131', '12132', \
          '12223', '12224', '12225', '12226', '12227', \
          '12228', '12229', '12230', '12231', '12232', \
          '12323', '12324', '12325', '12326', '12327', \
          '12328', '12329', '12330', '12331', \
          '12423', '12424', '12425', '12426', '12427', \
          '12428', '12429', '12430', '12431', \
          '12525', '12526', '12527', '12528', '12529', \
          '12530', '12531', \
          '12626', '12627']
    # LT5115033
    (qian, file1) = os.path.split(file1)
    to_pp = file1[3:6] + file1[7:9]
    to_pp = file1[3:6] + file1[8:10]
    print to_pp
    if to_pp in dh:
        return 1
    else:
        return 0



def extract_zip_file(file):
    unzip_cmd = 'tar xfvz ' + file + ' -C ' + TMP_DIR
    os.popen(unzip_cmd)
    pass
def clear_temp_files():
    rm_cmd = 'rm -rf ' + TMP_DIR + '/*'
    print ' ' * 4 + 'rm_cmd :' 
    print ' ' * 8 + rm_cmd
    os.popen(rm_cmd)
    
def band_merge(outfile):
    os.chdir(TMP_DIR)
    # if hao[0] == '5' or  hao[0] == '4':
    #     tif4 = glob.glob('*nn4*.tif')
    #     tif3 = glob.glob('*nn3*.tif')
    #     tif2 = glob.glob('*nn2*.tif')
    # else :
    tif4 = glob.glob('*nn40*.tif')
    tif3 = glob.glob('*nn30*.tif')
    tif2 = glob.glob('*nn20*.tif')
    if len(tif4) == 1 and len(tif3) == 1 and len(tif2) == 1:
        band4 = tif4[0]
        band3 = tif3[0]
        band2 = tif2[0]
        outfile_bandmerge = TMP_DIR + os.sep + 'bm.tif'
        print 'Generate: ' + outfile_bandmerge
        if os.path.exists(outfile_bandmerge):
            # 已经有文件的话则Pass
            pass
        else:
            band_merge_cmd = 'ossim-band-merge tiff_strip ' + band4 \
                + ' ' + band3 + ' ' + band2 + ' ' + \
                outfile
            u = os.popen(band_merge_cmd).read()
            print u
    else:
        # fo.write(ws + '\n')
        pass

def run(inws, outws):
    for root, dirs, files in os.walk(inws):
        for file in files:
            (qian, hou) = os.path.splitext(file)
            if hou.lower() == '.gz' and in_db(file) == 1:
                clear_temp_files()
                (qian, hou) = os.path.splitext(qian)
                outfile = outws + os.sep + qian + '.tif'
                infile = os.path.join(root, file)
                extract_zip_file(infile)
                band_merge(outfile)

if __name__ == '__main__':
    inws = '/home/bk/landsatorg/ETM'
    outws = '/home/bk/landsatorg432'
    if os.path.exists(outws):
        pass
    else:
        os.mkdir(outws)
    run(inws, outws)
