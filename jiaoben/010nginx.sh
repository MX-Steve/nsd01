#!/bin/bash
read -p '需要依赖包niginx-1.12.2.tar.gz，放在root目录下'
N=`yum repolist | awk '/repolist/{print $2}' | sed 's/,//g'`
if [ $N -le 0 ];then
	echo "YUM不可用"
	exit
fi
yum -y install gcc openssl-devel pcre-devel
tar -xf /root/nginx-1.12.2.tar.gz -C /root/
cd /root/nginx-1.12.2/
./configure
make
make install
