#!/bin/bash

yum -y install wget

yum -y install gcc openssl-devel bzip2-devel libffi-devel zlib-devel xz-devel 
cd /usr/src  

wget https://www.python.org/ftp/python/3.7.11/Python-3.7.11.tgz
tar xzf Python-3.7.11.tgz 

cd Python-3.7.11 
./configure --enable-optimizations 
make altinstall 

rm -f /usr/src/Python-3.7.11.tgz 

ln -s /usr/local/bin/python3.7 /usr/bin/python3.7
ln -s /usr/local/bin/pip3.7 /usr/bin/pip3.7

cd /root/


clear 

python3.7 -V 
which python3.7


