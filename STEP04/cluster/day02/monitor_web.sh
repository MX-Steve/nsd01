#!/bin/bash
VIP=192.168.4.100:80
RIP1=192.168.4.2
RIP2=192.168.4.3
while [ : ]
do
    for ip in $RIP1 $RIP2
    do
     curl http://$ip &>/dev/null
     web_health=$?
     ipvsadm -Ln | grep $ip &>/dev/null
     web_in_lvs=$?
     if [ $web_health -ne 0 -a $web_in_lvs -eq 0 ];then
     	ipvsadm -d -t $VIP -r $ip
     elif [ $web_health -eq 0 -a $web_in_lvs -ne 0 ];then
     	ipvsadm -a -t $VIP -r $ip
     fi
    done
    sleep 3
done
