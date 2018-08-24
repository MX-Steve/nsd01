import os
import time
pid=os.fork()
if pid:
    print("in parent,sleeping")
    time.sleep(20)
    print(os.waitpid(-1,1)) # 干掉自己的僵尸进程，如果子进程是僵尸进程，释放掉，如果不是僵尸进程，过
        #如果他之前的执行时间小于子进程，则waitpid无法杀出子进程，等父程序都执行完后释放给init或者systemd
    time.sleep(60)
else:
    print("in child, sleeping")
    time.sleep(15)
