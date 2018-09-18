FROM myos:v1
RUN  yum -y install initscripts openssh-server
ENV  EnvironmentFile=/etc/sysconfig/sshd
RUN  sshd-keygen 
RUN  echo 'aa' | passwd --stdin root
EXPOSE 22
CMD  ["/usr/sbin/sshd", "-D"]

