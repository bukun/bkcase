
fo = open('urls.txt', 'w')

with open('map.list') as fi:
    cnts = fi.readlines()
    for cnt in cnts:
        cnt = cnt.strip()
        if len(cnt) >0 :
            fo.write('http://www.maplet.org/map/{0}\n'.format(cnt))

with open('post.list') as fi:
    cnts = fi.readlines()
    for cnt in cnts:
        cnt = cnt.strip()
        if len(cnt) >0 :
            fo.write('http://www.maplet.org/post/{0}.html\n'.format(cnt))

fo.close()