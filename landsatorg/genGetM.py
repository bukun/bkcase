import os
import sys

fo = open('getfile.lftp', 'w')
fo.write('open ftp://imagery:imagery@35.8.163.34/\n')
fo.write('queue\n')
tps = ['MSS', 'TM', 'ETM']
tps = ['MSS']
for tp in tps:
    for lie in range(123,137):
        for hang in range(20, 41):
            cnt = 'queue mget -d -c ' + tp + '/' + str(lie) + '/0' + str(hang) + '/*\n'
            fo.write(cnt)
fo.write('queue start\n')
fo.close()

