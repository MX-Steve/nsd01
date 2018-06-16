#!/bin/bash
#单位都是kb
#提取根分区剩余空间
disk_size=`df / | awk '/\//{print $4}'`
#提取内存剩余空间
mem_size=`free | awk '/Mem/{print $4}'`
if [ $disk_size -le 512000 ];then
	mail -s diskWarning root <<EOF
磁盘空间不足!
EOF
exit
fi
if [ $mem_size -le 1024000 ];then
	mail -s memWarning root <<EOF
内存空间不足！
EOF
exit
fi
