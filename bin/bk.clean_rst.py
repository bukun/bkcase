# -*- coding: utf-8 -*-


import os
import shutil

'''
对图片进行自动处理。
'''

import os
import sys
import shutil
import re


def check_if_fig(instr):
    '''
    对条件进行判断
    '''

    if instr.startswith('.. image::'):
        # 直接引用的图片
        return True
    elif instr.startswith('.. figure::'):
        # 直接引用的图片
        return True
    elif instr.startswith('.. ') and ' image:: ' in instr:
        # 放到底部的图片
        return True

    return False


def fig_get_file_name(instr):
    tt = instr.strip().split()[-1]
    file_name = os.path.split(tt)[-1]
    zhui = os.path.splitext(file_name)[-1].lower()
    if zhui in ['.jpg', '.png', '.jpeg']:
        return file_name
    else:
        return None


def fig_get_file_path(inroot, wname):
    '''
    根据给定的路径，得到文件的路径
    找不到的話，就返回空字符串
    '''
    # print('x' * 20)
    # print(inroot)
    # print(wname)
    if wname.startswith('pa') or wname.startswith('ch'):
        # 对章节不处理
        return ''
    for wroot, wdirs, wfiles in os.walk(inroot):
        for wfile in wfiles:
            # 分别对两使用情况进行处理
            # 使用include的时候，可能不会包含.tex后缀
            #
            if wfile == wname:
                # print('y' * 10)
                outpath = os.path.join(wroot, wfile)
                # print(outpath)
                return outpath
            tt = os.path.splitext(wfile)[0]
            if tt == wname:
                # print('y' * 10)
                outpath = os.path.join(wroot, tt)
                # print(outpath)
                return outpath
    # print('not find')
    return 'occupy.png'


def clean_figs(inws):
    '''
    对rst文件中的图片，程序等引用外部文件的进行处理
    '''
    for wroot, wdirs, wfiles in os.walk(inws):
        if '_build' in wroot:
            continue
        for wfile in wfiles:
            if wfile.endswith('.rst'):
                # print(wfile)
                cur_file = os.path.join(wroot, wfile)

                # 使用临时文件写入，防止出现问题
                tep_name = os.path.join(wroot, 'tmp_' + wfile)
                cnts = open(cur_file).readlines()
                fo = open(tep_name, 'w')
                for cnt in cnts:
                    if check_if_fig(cnt) == True:
                        img_name = fig_get_file_name(cnt)
                        outpath = ''
                        if img_name:
                            outpath = fig_get_file_path(wroot, img_name)

                        if outpath == '':
                            pass
                        else:
                            # 根据当前路径处理
                            outpath = '.' + outpath[len(wroot):]
                            cnt = '{qian} {imgpath}\n'.format(
                                qian=' '.join(cnt.strip().split()[:-1]),
                                imgpath=outpath)

                    fo.write(cnt)
                fo.close()

                os.remove(cur_file)
                shutil.move(tep_name, cur_file)


##############################################################################################################


def do_for_chapter(secws):
    '''
    '''
    sec_list = os.listdir(secws)
    sec_list = [x for x in sec_list if x.startswith('sec') and not x.endswith('_files')]
    sec_list.sort()

    index = 1
    rst_new_list = []
    for sec_dir in sec_list:

        tt = re.split('[-_]', sec_dir)
        feaname = tt[1]

        outname = 'sec{0}-{1}'.format(str(index).zfill(2), feaname)

        inpath = os.path.join(secws, sec_dir)

        # 对于 section， 要区分是否文件
        if os.path.isfile(inpath):
            if outname.endswith('.rst'):
                pass
            else:
                # 在进行 split 时，有可能忽略了后缀
                outname = outname + '.rst'
            rst_new_list.append(outname)
        else:
            rst_new_list.append(os.path.join(outname, 'section.rst'))

        outpath = os.path.join(secws, outname)
        shutil.move(inpath, outpath)

        index = index + 1

    idxfile = os.path.join(secws, 'chapter.rst')
    if os.path.exists(idxfile):
        pass
    else:
        with open(idxfile, 'w') as fo:
            fo.write('''Chapter
==============================================

''')
    sec_cnt = open(idxfile).readlines()

    with open(idxfile, 'w') as fo:
        for uu in sec_cnt:
            if '.. toctree::' in uu:
                break
            else:
                fo.write(uu)
        fo.write('''.. toctree::\n   :maxdepth: 2\n\n''')
        for x in rst_new_list:
            fo.write('   {0}\n'.format(x))


def do_for_part(secws):
    sec_list = os.listdir(secws)
    sec_list.sort()

    index = 1
    rst_new_list = []
    for sec_dir in sec_list:
        if sec_dir.startswith('ch'):
            tt = re.split('[-_]', sec_dir)
            feaname = tt[1]

            outname = 'ch{0}-{1}'.format(str(index).zfill(2), feaname)
            index = index + 1
            rst_new_list.append(outname)
            inpath = os.path.join(secws, sec_dir)
            outpath = os.path.join(secws, outname)

            shutil.move(inpath, outpath)

    idxfile = os.path.join(secws, 'part.rst')
    if os.path.exists(idxfile):
        pass
    else:
        with open(idxfile, 'w') as fo:
            fo.write('''Part
==============================================

''')
    sec_cnt = open(idxfile).readlines()

    with open(idxfile, 'w') as fo:
        for uu in sec_cnt:
            if '.. toctree::' in uu:
                break
            else:
                fo.write(uu)
        fo.write('''.. toctree::\n   :maxdepth: 3\n   :numbered: 3\n\n''')
        for x in rst_new_list:
            fo.write('   {0}/chapter\n'.format(x))


def do_for_book(secws):
    sec_list = os.listdir(secws)
    sec_list = [x for x in sec_list if x[:2] in ['ch', 'pt']]
    sec_list.sort()

    index = 1
    rst_new_list = []
    for sec_dir in sec_list:
        tt = re.split('[-_]', sec_dir)
        print(tt)
        feaname = tt[1]
        if sec_dir.startswith('ch'):
            outname = 'ch{0}-{1}'.format(str(index).zfill(2), feaname)
        else:
            # for `part`.
            outname = 'pt{0}-{1}'.format(str(index).zfill(2), feaname)

        inpath = os.path.join(secws, sec_dir)
        outpath = os.path.join(secws, outname)

        shutil.move(inpath, outpath)

        rst_new_list.append(outname)

        index = index + 1

    if os.path.exists(os.path.join(secws, 'index.rst')):
        pass
    else:
        return False
    sec_cnt = open(os.path.join(secws, 'index.rst')).readlines()

    with open(os.path.join(secws, 'index.rst'), 'w') as fo:
        for uu in sec_cnt:
            if '.. toctree::' in uu:
                break
            else:
                fo.write(uu)


        if rst_new_list[0].startswith('ch'):
            fo.write('''.. toctree::\n   :maxdepth: 3\n   :numbered: 3\n\n''')
        else:
            fo.write('''.. toctree::\n\n''')

        for x in rst_new_list:
            if x.startswith('ch'):
                fo.write('   {0}/chapter\n'.format(x))
            else:
                fo.write('   {0}/part\n'.format(x))


def clean_book():
    '''
    do, one by one.
    '''

    for wroot, wdirs, wfiles in os.walk('./'):
        for wdir in wdirs:
            if wdir.startswith('sec'):
                inws = os.path.join(wroot, wdir)
                # do_for_section(inws)
    for wroot, wdirs, wfiles in os.walk('./'):
        for wdir in wdirs:
            if wdir.startswith('ch'):
                inws = os.path.join(wroot, wdir)
                do_for_chapter(inws)
    for wroot, wdirs, wfiles in os.walk('./'):
        for wdir in wdirs:
            if wdir.startswith('pt'):
                inws = os.path.join(wroot, wdir)
                do_for_part(inws)
    do_for_book(os.getcwd())


if __name__ == '__main__':
    fuws = os.path.join(os.getcwd())
    clean_book()
    clean_figs(fuws)
