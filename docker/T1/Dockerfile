FROM centos
RUN rm -rf /etc/yum.repos.d/*
ADD a.repo /etc/yum.repos.d/dvd.repo
RUN yum -y install psmisc net-tools vim
