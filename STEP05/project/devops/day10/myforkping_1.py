import os
import subprocess
def ping(host):
    result=subprocess.call(
        'ping -c2 %s &>/dev/null' %host,
        shell=True
    )
    if result == 0: # result的值就是ping函数的返回值，即$?
        print("%s:up" % host)
    else:
        print("%s:down" % host)


if __name__ == '__main__':
    ips=['176.4.13.%s' % i for i in range(1,255)]
    for ip in ips:
        pid=os.fork()
        if not pid:
            ping(ip)
            exit()