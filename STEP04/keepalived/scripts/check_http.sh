#!/bin/bash
curl http://192.168.4.2 &>/dev/null
if [ $? -ne 0 ];then
	systemctl stop keepalived
fi
