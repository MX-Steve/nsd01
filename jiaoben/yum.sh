#!/bin/bash
read -p "请输入要搭yum的主机ip：" ip
read -p "请输入要搭yum的主机密码：" pass
read -p "请输入yum源：" baseurl
rpm -q expect &>/dev/null
[ $? -ne 0 ] && yum -y install expect &>/dev/null
com="echo -e '\[dvd\] \nname=dvd \nbaseurl=$baseurl \ngpgcheck=0 \nenabled=1'>/etc/yum.repos.d/dvd.repo\n"
expect <<EOF
	spawn ssh -o StrictHostKeyChecking=no $ip
	expect "password" {send "$pass\n"}
	expect "#"	{send "rm -rf /etc/yum.repos.d/* \n"}
	expect "#"	{send "$com"}
	expect "#"	{send "yum clean all &>/dev/null \n"}
	expect "#"	{send "yum repolist | tail -1 | awk '{print $2}' \n"}
	expect "#"	{send "exit \n"}
EOF
