import os



cwd = os.getcwd()
the_dirs = os.listdir(cwd)
fthe_dirs = []
for the_dir in the_dirs:
    fthe_dir = os.path.join(cwd, the_dir)
    if os.path.isdir(the_dir):
        # print(fthe_dir)
        fthe_dirs.append((fthe_dir))

for fthe_dir in fthe_dirs:
    print('=' * 80)
    print(fthe_dir)
    os.chdir(fthe_dir)
    # os.popen('git pull')
    os.system('git pull')

os.chdir('/home/bk/opt/coding/book_ogc_standard/ogc_standard_rst')
os.system('source ~/vpy_rst/bin/activate')
os.system('make html')

os.chdir('/home/bk/opt/coding/book_webgis/webgis_rst')
os.system('source ~/vpy_rst/bin/activate')
os.system('make html')
