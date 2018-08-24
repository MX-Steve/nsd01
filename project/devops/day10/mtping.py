import subprocess
import os
import threading
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
    ips=['176.4.13.%s'% i for i in range(1,255)]
    for i in ips: #主线程
        t = threading.Thread(target=ping,args=(i,)) #子线程，干活，主线程不会等待工作线程结束,直接进入下一次循环
        t.start() # 执行ping(i),执行完就停止，不会有僵尸进程