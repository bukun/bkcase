# -*- coding:utf-8 -*-

# writer:xmnathan
# py文件去注释
import re
import os


Python = 'CleanNote'




def IsPassLine(strLine):
    # 是否是可以忽略的行
    # 可忽略行的正则表达式列表
    RegularExpressions = ["""/'.*#.*/'""", """/".*#.*/""",
                          """/'/'/'.*#.*/'/'/'""", """/"/"/".*#.*/"/"/"""]
    for One in RegularExpressions:
        zz = re.compile(One)
        if re.search(zz, strLine) == None:
            continue
        else:
            return True  # 有匹配 则忽略
        return False


def ReadFile(FileName):
    # 读取并处理文件
    fobj = open(FileName, 'r')
    AllLines = fobj.readlines()
    fobj.close()
    NewStr = ''
    LogStr = '/n%20s/n' % (FileName.split('//')[-1])  # 输出的日志
    nline = 0
    for eachline in AllLines:
        index = eachline.find('#')  # 获取带注释句‘#’的位置索引
        if index == -1 or nline < 3 or IsPassLine(eachline):
            if eachline.strip() != '':  # 排除纯空的行
                NewStr = NewStr + eachline
        else:
            if index != 0:
                NewStr = NewStr + eachline[:index] + '/n'  # 截取后面的注释部分
                LogStr += "ChangeLine: %s/t%s" % (nline, eachline[index:])
        nline += 1
    return NewStr, LogStr


def MakeCleanFile(SrcPath, DescPath, FileList):
    # fLog=open(DescPath+'//'+'CleanNoteLog.txt','w')
    for File in FileList:
        curStr, LogStr = ReadFile(SrcPath + '/' + File)
        fNew = open(DescPath + '/' + File, 'w')
        fNew.write(curStr)
        fNew.close()
        # fLog.write(LogStr)
        # fLog.close()


def Main():
    # 从ini获取源文件夹及目标文件夹路径

    SrcPath = '/Users/bukun/github/TorCMS/torcms'
    DescPath = '/Users/bukun/tmp/xxtorcms'
    # 如果目的文件夹不存在，创建之
    if not os.path.exists(DescPath):
        os.makedirs(DescPath)
    FileList = []
    for wroot, wdirs, wfiles in os.walk(SrcPath):
        for FileName in wfiles:
            if FileName.split('.')[-1] == 'py':

                infile = os.path.join(wroot, FileName)
                outfile = os.path.join(DescPath, infile[len(SrcPath) + 1:])

                outpath = os.path.split(outfile)[0]
                if os.path.exists(outpath):
                    pass
                else:
                    os.makedirs(outpath)

                print(outfile)

                curStr, LogStr = ReadFile(infile)

                fNew = open(outfile, 'w')
                fNew.write(curStr)
                fNew.close()
                # FileList.append(FileName)
    # MakeCleanFile(SrcPath, DescPath, FileList)


if __name__ == '__main__':
    Main()
    print('>>>End<<<')
