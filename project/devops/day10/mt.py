#多线程：包含在一个进程内，没有僵尸进程问题，共用进程资源
import time
import os

def calc():
    result = 0
    for i in range(50000000):
        result +=i
    print(result)

if __name__ == '__main__':
    # start = time.time()
    # calc()
    # calc()
    # end=time.time()
    # print(end-start)
    ####################################################
    start = time.time()
    pid=os.fork()
    if not pid:
        calc()
        exit()
    pid=os.fork()
    if not pid:
        calc()
        exit()
    os.waitpid(-1,0) #父挂起
    os.waitpid(-1, 0)
    end = time.time()
    print(end-start)