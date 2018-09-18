#多线程：包含在一个进程内，没有僵尸进程问题，共用进程资源

#多进程
#cpu多核心，一个进程在一个核心上，另外一个进程在第二个核心上

#GIL:全局解释器锁
#GIL的存在导致某一时刻只能把一个线程交给cpu处理

import time
import os
import threading

def calc(n=50000000):
    result = 0
    for i in range(n):
        result +=i
    print(result)

if __name__ == '__main__':
    # start = time.time()
    # calc()
    # calc()
    # end=time.time()
    # print(end-start)
    ####################################################
    # start = time.time()
    # pid=os.fork()
    # if not pid:
    #     calc()
    #     exit()
    # pid=os.fork()
    # if not pid:
    #     calc()
    #     exit()
    # os.waitpid(-1,0) #父挂起
    # os.waitpid(-1, 0)
    # end = time.time()
    # print(end-start)
    ####################################################
    start = time.time()
    n=10000
    t1 = threading.Thread(target=calc,args=(n,))
    t1.start()
    t2=threading.Thread(target=calc,args=(n,))
    t2.start()
    t1.join()
    t2.join() #线程中没有僵尸线程，只是挂起主线程，等到t1线程结束后再向下指向
    end=time.time()
    print(end-start)