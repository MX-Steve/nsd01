#!/bin/bash
yum -y install vsftpd &>/dev/null
cp /etc/vsftpd/vsftpd.conf{,.bak}
sed -i 's/^#an/an/' /etc/vsftpd/vsftpd.conf
chmod 777 /var/ftp/pub/
systemctl restart vsftpd &>/dev/null
systemctl enable vsftpd &>/dev/null
echo "ok"
