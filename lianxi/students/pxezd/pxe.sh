#!/bin/bash
echo "检查yum是否配置..."
yum clean all &> /dev/null
yums=`yum  repolist|awk 'END{print $2}'`

sleep 1
if [ $yums != "0" ];then
	echo "yum已正确安装！"
else
	rm -rf /etc/yum.repos.d/*
	echo "[dvd]
name=dvd
baseurl=ftp://192.168.4.254/rhel7
enabled=1
gpgcheck=0" > /etc/yum.repos.d/dvd.repo
echo "已自动配置yum!"
fi
ip=`ifconfig |grep inet |awk 'NR==1{print $2}'`
echo "安装包中。。。"
yum -y install dhcp syslinux tftp-server httpd &> /dev/null
echo "安装包已经安装完毕！"
echo "subnet 192.168.4.0 netmask 255.255.255.0 {
  range 192.168.4.100 192.168.4.150;
  option domain-name-servers $ip;
  option routers 192.168.4.254;
  default-lease-time 600;
  max-lease-time 7200;
  next-server $ip;
  filename \"pxelinux.0\";
}" > /etc/dhcp/dhcpd.conf
rm -rf /var/lib/tftpboot/*
cp /usr/share/syslinux/pxelinux.0 /var/lib/tftpboot/
mkdir /var/lib/tftpboot/pxelinux.cfg
#把iso文件放入cdrom
mkdir /mnt &> /dev/null
mount /dev/cdrom /mnt &> /dev/null
cp /mnt/isolinux/isolinux.cfg /var/lib/tftpboot/pxelinux.cfg/default &>/dev/null
if [ $? -ne 0 ];then
	echo "请插入光盘！"&& exit
fi
chmod 644 /var/lib/tftpboot/pxelinux.cfg/default
cp /mnt/isolinux/vesamenu.c32 /var/lib/tftpboot
cp /mnt/isolinux/splash.png /var/lib/tftpboot
cp /mnt/isolinux/vmlinuz /var/lib/tftpboot
cp /mnt/isolinux/initrd.img /var/lib/tftpboot
echo "菜单文件已准备就绪！"
sed -i '64,$d' /var/lib/tftpboot/pxelinux.cfg/default
sed -i '63a append initrd=initrd.img ks=http://'$ip'/ks.cfg' /var/lib/tftpboot/pxelinux.cfg/default
sed -i '62a menu default' /var/lib/tftpboot/pxelinux.cfg/default
mkdir /var/www/html/rhel7 &> /dev/null
mount /dev/cdrom /var/www/html/rhel7 &>/dev/null
sed -i '9a url --url="http://'$ip'/rhel7"' ks.cfg
sed -i '11d' ks.cfg
cp ./ks.cfg /var/www/html
systemctl restart httpd tftp dhcpd
echo "环境已准备就绪！"
