#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
import sys

def getindex ( secfile):
    '''
    得到要输出的行数索引列表
    '''
    index = []
    cnts = file(secfile).readlines()
    uu = 0
    allen = len(cnts)
    for cnt in cnts:
        if cnt.startswith('\section'):
            index.append(uu)
        uu = uu + 1
    index.append(allen)
    ind = [0] + index[:-1]
    uu = [(x, y) for x, y in zip(ind, index)]
    return uu
def get_file_list(secfile):
    '''
    得到要输出的文件名列表
    '''
    (pathto, filename) = os.path.split(secfile)
    (qian , hou) = os.path.splitext(filename)
    pwd = os.path.join(pathto, qian)
    if os.path.exists(pwd):
        pass
    else:
        os.mkdir(pwd)
    # 得到文件内容，以便分析
    cnts = file(secfile).readlines()
    # 一个索引，用于生成文件名与文件夹名
    dirindex = 10
    secfile = os.path.join(pwd, filename)
    outfiles = [secfile]
    for cnt in cnts:
        if cnt.startswith('\section'):
            # subsec的文件名
            subsec_name = 'sec%s.tex' % (str(dirindex).zfill(3))
            dirindex += 10
            subsec_path = os.path.join(pwd, subsec_name)
            outfiles.append(subsec_path)
    return(outfiles)
def output(secfile, wfiles, ind):
    '''
    根据输入内容
    输出文件名列表与索引列表
    生成输出文件
    '''
    cnts = file(secfile).readlines()
    for wfile, index in zip(wfiles, ind):
        fo = open(wfile, 'w')
        cnt = cnts[index[0]:index[1]]
        fo.writelines(cnt)
        fo.write('%----%\n')
        fo.close()
if __name__ == '__main__':
    inws = os.getcwd()
    secfiles = os.listdir(inws)
    for secfile in secfiles:
        if secfile.startswith('ch') and    secfile.endswith('tex'):
            secfile = os.path.join(inws, secfile)
            wfiles = get_file_list(secfile)
            print(wfiles)
            ind = getindex(secfile)
            print(ind)
            output(secfile, wfiles, ind)
