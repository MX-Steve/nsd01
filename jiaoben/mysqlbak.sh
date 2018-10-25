!/bin/bash
# W 第几周
# d 周几
# dir 备份目录

W=`date +%W`
d=`date +%w`
dir='/mysqlback/'
user="root"
password="123qqq...A"
[ -d ${dir}${W} ] || mkdir -p ${dir}${W}/$d
if [ $d -eq 1 ] ; then
	innobackupex --user=$user --password=$password ${dir}${W}/$d --no-timestamp
else 
	innobackupex  --user=$user --password=$password --incremental ${dir}${W}/$d --incremental-basedir=${dir}${W}/$[d-1] --no-timestamp
fi

