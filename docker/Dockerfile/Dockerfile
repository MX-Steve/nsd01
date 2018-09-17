FROM centos:latest
RUN  rm -rf /etc/yum.repos.d/*
ADD  dvd.repo /etc/yum.repos.d/dvd.repo
RUN  yum -y install net-tools iproute vim-enhanced psmisc
