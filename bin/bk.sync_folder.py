#!/usr/bin/env python3
#-*-encoding:utf-8-*-
"""
    Compare the files between two folders.
    And will delete one if they are the same.
"""
import os, hashlib, io, sys, glob

def get_md5_value(filename):
    """
        To get the MD5 value.
    """
    mdval = hashlib.md5()
    filein = io.FileIO(filename, 'r')
    bytesseg = filein.read(1024)
    while ( bytesseg != b'' ) :
        mdval.update(bytesseg)
        bytesseg = filein.read(1024)
    filein.close()
    md5value = mdval.hexdigest()
    return md5value

def del_double_files(folder1, folder2):
    """
      Compare between two folders.
    """
    foler1_name_length = len(folder1) # The name length of folder1. 
    for root, dirs, files in os.walk(folder1):
        for filename in files:
            file1 = os.path.join(root, filename)
            file2 = folder2 + file1[foler1_name_length:]
            if os.path.islink(file1):
                print('link: %s', (file1))
                os.remove(file1)
            elif os.path.exists(file2) :
                del_double_file(file1, file2)
def del_double_file(file1, file2):
    """
      Delete one file if they are the same. 
      第一个是要被删除的
    """
     
    md5a = get_md5_value(file1)
    md5b = get_md5_value(file2)
    if md5a == md5b:
        # print " " * 10 + file2
        os.remove(file1)
    else:
        pass
def is_empry_directory(dirpath):
    # os.chdir(dirpath)
    # tepFiles  = glob.glob('*')
    tepFiles = os.listdir(dirpath)
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
                print (fullpath)
                try:
                    os.rmdir(fullpath)
                except:
                    pass
                # fo.write('rmdir "' + fullpath + '"\n')
            else:
                del_empty_folder(fullpath)
        else:
            (path2file, filename) = os.path.split(fullpath)
            (filename, houzhui) = os.path.splitext(filename)
            if houzhui.lower() == '.tif':
                # buildPyramids(fullpath)
                # print fullpath
                pass
            else:
                pass

   
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage:")
        print(' ' * 4 + "bk.sync_folder keep_dir del_dir")
        sys.exit()
    # The file to be delete. 
    FOLDER1 = sys.argv[2]
    # The files will be kept.
    FOLDER2 = sys.argv[1]
    # FOLDER2 = '/v/osx/FragstatsGCC3' 
    FOLDER1 = os.path.abspath(FOLDER1)
    FOLDER2 = os.path.abspath(FOLDER2)
    if FOLDER1 == FOLDER2:
        sys.exit()
    else:
        if os.path.exists(FOLDER2):
            del_double_files(FOLDER1, FOLDER2)
    for i in range(1,20):
        del_empty_folder(FOLDER1)
