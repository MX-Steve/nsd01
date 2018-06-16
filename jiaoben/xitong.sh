#!/bin/bash
#查看主机系统信息

echo "主机名：" `hostname`
echo "ip地址与子网掩码：" `ifconfig | awk 'NR==2{print $2,$4}'`
echo "系统版本：" `cat /etc/redhat-release`
echo "运行内存：" `awk '/MemTotal/{print $2$3}' /proc/meminfo`
echo "当前连接该服务器的用户：" `who | awk '{print $1 $5}'`
