#!/bin/bash
case $1 in
start)
	/usr/local/nginx/sbin/nginx;;
stop)
	/usr/local/nginx/sbin/nginx -s stop;;
restart)
	/usr/local/nginx/sbin/nginx -s stop
	/usr/local/nginx/sbin/nginx;;
status)
	netstat -anptu | grep -q nginx
	if [ $? -eq 0 ];then
echo 服务已经启动
else
echo 服务没有启动
fi;;
*)
	echo ERROR;;
esac
