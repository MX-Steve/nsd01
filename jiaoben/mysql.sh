#!/bin/bash
read -p 'IP:' ip
expect <<EOF
spawn ssh -o "StrictHostKeyChecking=no" $ip
set timeout 300
expect "assword" {send "123456\n"}
expect "#"	{send "rm -rf mysql\n"}
expect "#"	{send "mkdir mysql\n"}
expect "#"	{send "tar -xf mysql-5.7.17.tar -C mysql/\n"}
expect "#"	{send "cd mysql\n"}
expect "#"	{send "yum -y install *.rpm\n"}
expect "]#"	{send "systemctl restart mysqld\n"}
expect "#"	{send "systemctl enable mysqld\n"}
expect "#"	{send "exit\n"}
EOF
