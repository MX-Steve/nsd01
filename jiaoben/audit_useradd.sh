#!/bin/bash
#comment=`ausearch -f /etc/passwd | grep useradd | tail -1`
timer=`ausearch -f /etc/passwd | grep useradd | tail -1 | awk '{print $2}' | awk -F'[(.)]' '{print $2}'`
timer=`date -d @$timer +%F-%Hh`
uid=`ausearch -f /etc/passwd | grep useradd | tail -1 | awk '{print $15}' | awk -F'=' '{print $2}'`
uname=`awk -F: '$3=='$uid'{print $1}' /etc/passwd`
ppid=`ausearch -f /etc/passwd | grep useradd | tail -1 | awk '{print $12}' | awk -F'=' '{print $2}'`
addr=`cat /var/log/audit/audit.log |grep "$ppid"| grep hostname | tail -1 | awk '{print $12}'|awk -F'=' '{print $2}'`
WhoIsCreated=`tail -1 /etc/passwd | awk -F: '{print $1}'`

echo $timer $uname $addr $WhoIsCreated >> /root/a.txt 
