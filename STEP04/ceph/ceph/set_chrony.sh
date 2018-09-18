#!/bin/bash
#该脚本在node1节点上执行

#无密连接
rpm -q expect &>/dev/null
[ $? -ne 0 ] && yum -y install expect &>/dev/null

ssh-keygen -f /root/.ssh/id_rsa -N ""
source wumi.sh
source wumi.sh
echo "无密连接创建成功！"

#时间同步
sed -i "s/^#allow.*/allow 192.168.4.0\/24/" /etc/chrony.conf
sed -i "s/^#local/local/" /etc/chrony.conf

systemctl restart chronyd &>/dev/null
systemctl enable chronyd &>/dev/null

for node in 192.168.4.{1,3,4,5,6}
do
	ssh $node sed -i "s/^server/#server/" /etc/chrony.conf
	ssh $node sed -i "1a'server 192.168.4.2 iburst'" /etc/chrony.conf
	ssh $node systemctl restart chronyd &>/dev/null
	ssh $node systemctl enable chronyd &>/dev/null
	sleep 5
done

echo "时间同步完成，时间服务器为node1"
