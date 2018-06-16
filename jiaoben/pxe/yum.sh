rm -rf /etc/yum.repos.d/*
echo '[development]
name=development
baseurl=http://192.168.4.254/rhel7
gpgcheck=0
enabled=1'>/etc/yum.repos.d/dvd.repo
yum clean all
yum repolist
