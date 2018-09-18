FROM    myos:v1
RUN     yum -y install httpd
WORKDIR /var/www/html
RUN     echo 'hello world' >index.html
EXPOSE  80
ENV     EnvironmentFile=/etc/sysconfig/httpd
CMD     ["/usr/sbin/httpd",  "-DFOREGROUND"]

