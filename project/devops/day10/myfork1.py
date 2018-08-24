import os
import time
for i in range(3):
    pid=os.fork()#父进程负责生成子进程
    if not pid:
        print("hello")
        exit() #子进程遇到exit结束，不会回到循环条件处
        # time.sleep(5)