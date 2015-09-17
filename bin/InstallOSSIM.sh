#如果你不安装ossim删除下面就可以了。
echo "start install OSSIM--an opensourse remote sensing software"
sudo aptitude install subversion -y
sudo aptitude install libtiff-dev -y
sudo aptitude install libgeotiff-dev -y
sudo aptitude install libopenthreads-dev -y
sudo aptitude install libgdal-dev -y
sudo ldconfig
mkdir /tmp/ossim
cd /tmp/ossim
svn co http://svn.osgeo.org/ossim/trunk .
cd ossim
./configure --enable-singleStaticOssimLibrary=yes --enable-staticOssimApps
make depends
make
sudo make install
sudo aptitude install qt3-dev-tools -y
cd /tmp/ossim/ossim_qt
qmake
make
sudo make install
echo "OSSIM installation end! Using QT3-interfaces"

