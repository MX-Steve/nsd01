#!/bin/bash
#mymaster leader start 192.168.1.20 6379 192.168.1.21 6379
VIP="192.168.1.50/24"
local_ip=$(ip  addr show dev eth0 |awk '$1=="inet"{print $2}')
if [[ "${local_ip%%/*}" == "$4" ]];then
   /usr/sbin/ifconfig eth0:1 down
elif [[ "${local_ip%%/*}" == "$6" ]];then
   /usr/sbin/ifconfig eth0:1 "${VIP}"
fi

