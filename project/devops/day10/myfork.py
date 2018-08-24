# print('starting')
# print('hello world')

import os
import time
# print("starting")
# #生成子进程，后续代码在子进程和父进程同时运行
# os.fork()
# print("hello world")
# print("ending")

print("starting")

pid=os.fork() # 父进程返回值是子进程的pid，子进程返回值是0
# 父进程：1348 子进程 0
if pid:
    time.sleep(5)
    print("in parent")

else:
    print("in child")

print('done')