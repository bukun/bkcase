# -*- coding:utf-8 -*-
import os
import sys
import shutil
import glob
def test_zipfile(zipfile):
    '''
      To test a zipfile is right.
    '''
    print 'Test file: ' + zipfile
    testcmd = '7z t ' + zipfile
    re = os.popen(testcmd).readlines()
    re2 = [x.replace('\n', '') for x in re]
    if len(re2) < 9:
        print gz
        return 0
    else:
        if re2[8].lower() == 'Everything is Ok'.lower():
            print "    OK:" + zipfile
            return 1
        else:
            return 0
def clear_temp_dir(temp_dir):
    '''
      Delete everything in temp_dir.
    '''
    rm_cmd = 'rm -rf ' + temp_dir + os.sep + '*'
    print rm_cmd
    echo = os.popen(rm_cmd).read()
    print echo

def unzip_file(zipfile, outdir):
    '''
       Extract files in a zipfile to a certain directory.
    '''
    unzip_cmd = 'tar xfvz ' + zipfile + ' -C ' + outdir
    print 'Extract file: ' + zipfile
    echo = os.popen(unzip_cmd).read()
    print echo
def enhance(infile, outfile):
    print 'Enhance file: ' + infile
    enhance_cmd = 'gdalenhance -of GTiff -ot Byte -equalize ' \
        + infile + ' ' +  outfile
    u = os.popen(enhance_cmd).read()
    print u

def band_merge(indir, outfile):
    os.chdir(indir)
    tif4 = glob.glob('*nn40*.tif')
    tif3 = glob.glob('*nn30*.tif')
    tif2 = glob.glob('*nn20*.tif')
    if len(tif4) == 1 and len(tif3) == 1 and len(tif2) == 1:
        band4 = tif4[0]
        band3 = tif3[0]
        band2 = tif2[0]
    print 'Generate: ' + outfile
    if os.path.exists(outfile):
        # 已经有文件的话则Pass
        print 'File exists: ' + outfile
        pass
    else:
        band_merge_cmd = 'ossim-band-merge tiff_strip ' + band4 \
            + ' ' + band3 + ' ' + band2 + ' ' + \
            outfile
        u = os.popen(band_merge_cmd).read()
        print u
if __name__ == '__main__':
    FUWS = '/home/bk/landsatorg'
    temp_dir = '/home/bk/v'
    for root, dirs, files  in os.walk(FUWS):
        for file in files:
            (qian, hou) = os.path.splitext(file)
            (qian, tep) = os.path.splitext(qian)
            if hou == '.gz':
                zipfile = os.path.join(root, file)
                outfile = os.path.join(root, qian) + '.tif'
                if  os.path.exists(outfile) == False \
                        and test_zipfile(zipfile ) == 1 :
                    clear_temp_dir(temp_dir)
                    unzip_file(zipfile, temp_dir)
                    outfiletep = temp_dir + os.sep + 'xx_' + file + '.tif'
                    band_merge(temp_dir, outfile)
                    # enhance(outfiletep, outfile )

