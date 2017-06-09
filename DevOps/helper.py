# -*- coding: utf-8 -*-
import os
from fabric.api import get
import datetime
from fabric.context_managers import cd, settings
from fabric.operations import run

from cfg import coding_prompts


def backup_db(db, passwd):
    now = datetime.datetime.now()
    sig = now.strftime('%Y%m%d')
    fname = 'pg_{db}_{sig}'.format(db=db, sig=sig)
    with cd('~/tmp'):  # cd用于进入某个目录
        with settings(prompts={"Password: ": passwd, }):
            run('pg_dump -h localhost -U {db}  -F c {db}  > {fname}.bak'.format(fname=fname, db=db))
        run("tar -czf {fname}.tar.gz {fname}.bak".format(fname=fname))
        get('/home/bk/tmp/{fname}.tar.gz'.format(fname=fname), '/home/bk/tmp/{fname}.tar.gz'.format(fname=fname))
        # get('/home/bk/tmp/{fname}.tar.gz'.format(fname=fname), '//Users/bukun/bak/{fname}.tar.gz'.format(fname=fname))


def update_proj(projdic):
    print('=' * 40)
    print(' ' * 4 + projdic['projws'])
    with cd(os.path.join(projdic['projws'], 'templates/modules')):
        run('git pull')
    with cd(projdic['projws']):
        with settings(prompts=coding_prompts):
            run('git pull')
        run('{pip} install doc/requirements.txt'.format(pip=os.path.join(projdic['vpy'], 'bin/pip3')))
        run('{python} helper.py -i init'.format(python= os.path.join(projdic['vpy'], 'bin/python3')))
