FROM myos:v1
RUN yum -y install openssh-server
RUN echo "ooxx" | passwd --stdin root
ENV EnvironmentFile=/etc/sysconfig/sshd
RUN /usr/sbin/sshd-keygen
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
