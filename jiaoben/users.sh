#!/bin/bash
users=`awk -F: '/bash$/{print $1}' /etc/passwd`
for i in $users
do
	grep $i /etc/shadow | awk -F: '{print $1,$2}'
done
