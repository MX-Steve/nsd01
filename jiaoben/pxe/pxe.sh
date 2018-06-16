#!/bin/bash
#提供DHCP服务器的ip地址
SERVER=192.168.4.207
#step 1) DHCP
killall -9 dnsmasq &>/dev/null
yum -y install dhcp &>/dev/null
echo 'subnet 192.168.4.0 netmask 255.255.255.0 {
      range 192.168.4.100 192.168.4.200;
      next-server '$SERVER';
      filename "pxelinux.0";
      option domain-name-servers '$SERVER';
      default-lease-time 600;
      max-lease-time 7200;
    }'>/etc/dhcp/dhcpd.conf
systemctl restart dhcpd
echo 'DHCP搭建成功'

#step 2) TFTP
yum -y install tftp-server &>/dev/null
systemctl restart tftp
tar -xPf ./tftp.tar.gz 
echo 'TFTP搭建成功'

#step 3) HTTP
yum -y install httpd &>/dev/null
systemctl restart httpd
tar -xPf ./html.tar.gz
echo 'HTTP搭建成功'

