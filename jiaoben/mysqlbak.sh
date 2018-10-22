#!/bin/bash
# W 第几周
# d 周几
# full 备份目录

W=`date +%W`
d=`date +%w`
full='/mysqlback/'
user="root"
password="123qqq...A"
[ -d ${full}${W} ] || mkdir -p ${full}${W}/$d
if [ $d -eq 1 ] ; then
	innobackupex --user=$user --password=$password ${full}${W}/$d --no-timestamp
else 
	innobackupex  --user=$user --password=$password --incremental ${full}${W}/$d --incremental-basedir=${full}${W}/$[d-1] --no-timestamp
fi

