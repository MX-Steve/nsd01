#!/usr/bin/env python3
import time
import sys
def pao():
    l=19 # #号长度
    print("#"*(l+1),end='')
    counter=0
    while True:
        sys.stdout.flush()
        time.sleep(0.5)
        print("\r%s\033[32;1m@\033[0m%s"%("#"*counter,"#"*(l-counter)),end='')
        counter+=1
        if counter > l:
            counter=0
            print()

if __name__ == '__main__':
    pao()
    pao()