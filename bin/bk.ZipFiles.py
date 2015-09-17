#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
"""
  压缩某一文件夹下所有的文件，
  并删除掉原始文件
  文件存在在原来位置

  注意：
  程序对文件名中有特殊字符的处理不好，如空格、括号等
"""
import os
import sys
#
# 生成输出的文件名
#
def generate_output_name(filepatha):
    """
      根据输入的文件名，返回要生成的文件名
      路径为在原来的位置
    """
    outzipfile = filepatha + '.7z'
    return outzipfile

def zip_file(filepath):
    """
      压缩文件
    """
    outzipfile = generate_output_name(filepath )
    scmd = r'7z a "' + outzipfile + '" ' + filepath # 7zip命令行  
    print scmd
    try:
        sdir = os.popen(scmd).read()    #读取返回结果
    except:
        print sdir
        print "Error"
        return
    print '-' * 80
    # print filepath
    while os.path.exists(filepath) and os.path.exists(outzipfile):
        os.remove(filepath)

if __name__ == '__main__':
    inws = sys.argv[1]
    typeit = sys.argv[2]
    # CURPATH = r'/bk/Music/dj'  # 要压缩的文件父文件夹
    #os.chdir(CURPATH)
    FILENAMES = os.listdir(inws)
    for filename in FILENAMES:
        if filename.endswith(typeit):
            pass
        else:
            continue
        filepathin = inws + os.sep + filename
        if os.path.isfile:
            zip_file(filepathin)
