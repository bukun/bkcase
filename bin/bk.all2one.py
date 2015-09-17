#!/usr/bin/python
#-*-encoding:utf-8-*-
"""
    Compare the files between two folders.
    And will delete one if they are the same.
"""
import os, hashlib, io, sys, glob, shutil

def is_empry_directory(dirpath):
    os.chdir(dirpath)
    tepFiles  = glob.glob('*')
    if len(tepFiles) == 0 :
        return 1
    else:
        return 0     
                
def del_empty_folder(dir):
    os.chdir(dir)
    listnames = os.listdir(dir)
    for listname in listnames:
        fullpath = dir + os.sep + listname
        if os.path.isdir(fullpath):
            if is_empry_directory(fullpath) == 1 :
                print fullpath
                try:
                    os.rmdir(fullpath)
                except:
                    pass
                # fo.write('rmdir "' + fullpath + '"\n')
            else:
                del_empty_folder(fullpath)

def all2one(inws, outws):
   for wroot, wdirs , wfiles in os.walk(inws):
       for wfile in wfiles:
           infile = os.path.join(wroot, wfile)
           outfile = os.path.join(outws, wfile)
           if os.path.exists(outfile):
               pass
           else:
               shutil.move(infile, outfile)
  
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage:")
        print(' ' * 4 + "bk.all2one in_dir out_dir")
        sys.exit()
    # The file to be delete. 
    FOLDER1 = sys.argv[1]
    # The files will be kept.
    FOLDER2 = sys.argv[2]
    # FOLDER2 = '/v/osx/FragstatsGCC3' 
    FOLDER1 = os.path.abspath(FOLDER1)
    FOLDER2 = os.path.abspath(FOLDER2)
    if os.path.exists(FOLDER2):
        pass
    else:
        os.mkdir(FOLDER2)
    if FOLDER1 == FOLDER2:
        sys.exit()
    else:
        if os.path.exists(FOLDER2):
            all2one(FOLDER1, FOLDER2)
    for i in range(1,20):
        del_empty_folder(FOLDER1)
