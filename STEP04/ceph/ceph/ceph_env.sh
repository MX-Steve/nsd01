#!/bin/bash 
echo "ceph为redhat专有！"
# 准备osd存储盘，node1-3各三块10G存储盘
for node in ceph{2..4}
do
	qemu-img create -f qcow2 /var/lib/libvirt/images/$node-1.img 10G
	qemu-img create -f qcow2 /var/lib/libvirt/images/$node-2.img 10G
	qemu-img create -f qcow2 /var/lib/libvirt/images/$node-3.img 10G
done

#创建6台虚拟机后端镜像
for node in ceph{1..6}
do
	qemu-img create -f qcow2 -b /var/lib/libvirt/images/.rh7_template.img /var/lib/libvirt/images/$node.img &> /dev/null
done

#创建node1-3的xml文件并启用
for node in ceph{2..4}
do
	sed "s/rh7_template/$node/" ./.rhel7_3d.xml >/etc/libvirt/qemu/$node.xml
	virsh define /etc/libvirt/qemu/$node.xml
	virsh start $node
	virsh destroy $node
done

#创建client和node4-5三台xml文件并启用
for node in ceph{1,5,6}
do
	sed "s/rh7_template/$node/" ./.rhel7.xml >/etc/libvirt/qemu/$node.xml
        virsh define /etc/libvirt/qemu/$node.xml
        virsh start $node
	virsh destroy $node
done

#修改刚刚创建的6台主机的主机名和ip地址
#set_ip.sh是用来配置ip地址和主机名,hosts,yum源的函数
source ./set_ip.sh
yum install libguestfs libguestfs-tools -y &>/dev/null
for node in ceph{1..6}
do
	#if [ $node == "ceph1" ];then
	#	set_ip $node "192.168.4.1"	
	#elif [$node == ""]
	case $node in
	"ceph1")
		set_ip $node "192.168.4.1" "client"
		;;
	"ceph2")
		set_ip $node "192.168.4.2" "node1"
                ;;
	"ceph3")
		set_ip $node "192.168.4.3" "node2"
                ;;
	"ceph4")
		set_ip $node "192.168.4.4" "node3"
                ;;
	"ceph5")
		set_ip $node "192.168.4.5" "node4"
                ;;
	"ceph6")
		set_ip $node "192.168.4.6" "node5"
                ;;
	esac
done

#启动所有虚拟机，node1即ceph为管理机
for node in ceph{1..6}
do
	virsh start $node
done

#安装expect，连接node1，进行无密连接，时间同步等操作
echo "等待管理节点node1开机"
sleep 30
rpm -q expect &>/dev/null
[ $? -ne 0 ] && yum -y install expect &>/dev/null
expect <<EOF
	spawn scp ./set_chrony.sh ./wumi.sh 192.168.4.2:/root/
	expect "yes/no"		{send "yes\n"}
	expect "password"	{send "123456\n"}
	expect "#"		{send "exit\n"}
EOF
expect <<EOF
	spawn ssh 192.168.4.2
	expect "password"	{send "123456\n"}
	expect "]#"		{send "/root/set_chrony.sh\n"}
	expect "]#"		{send "/root/set_chrony.sh\n"}
	expect "]#"		{send "exit\n"}
EOF














