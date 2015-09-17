# author: bukun
#
import os
import sys

pwd = os.getcwd()

fo = open('clean_link.sh', 'w')
for wroot, wdirs, wfiles in os.walk(pwd):
    for wfile in wfiles:
        test = os.path.join(wroot, wfile)
        if os.path.islink(test):
            print(test)
            fo.write('rm -f %s\n' % test)
    for wdir in wdirs:
        test = os.path.join(wroot, wdir)
        if os.path.islink(test):
            print(test)
            os.remove(test)
            fo.write('rm -f %s\n' % test)
fo.close()
