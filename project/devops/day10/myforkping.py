import subprocess
import os
def ping(host):
    result=subprocess.call(
        "ping -c2 %s &>/dev/null" %host,
        shell=True
    )
    if result == 0:
        print("%s:up" % host)
    else:
        print("%s:down" % host)

if __name__ == '__main__':
    ips = ['176.4.13.%s' % i for i in range(1,255)]
    for ip in ips:
        pid=os.fork()
        if not pid:
            ping(ip) #子进程ping完一个地址后断开链接
            exit()