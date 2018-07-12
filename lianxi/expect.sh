#!/bin/bash
expect <<EOF
spawn ssh -o StrictHostKeyChecking=no 192.168.4.2
expect "password:" {send "123456\r"}
expect "#" {send "touch /tmp.txt\r"}
expect "#" {send "exit\r"}
EOF
