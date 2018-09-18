FROM myos:v1
RUN  yum -y install httpd
ADD index.html /var/www/html/index.html
EXPOSE 80
CMD ['/usr/sbin/httpd']
