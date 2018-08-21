"""
\r:回车步换行,打印的时候原位覆盖
"""
import time
import sys
# for i in range(1,11):
#     print("\r%s" %i,end='')
#     time.sleep(1)
print("===========================")

def pao():
    l = 19
    print('#'*(l+1),end='')
    counter=0
    while True:
        sys.stdout.flush()
        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            print()
            break
        print("\r%s@%s"%("#"*counter,"#"*(l-counter)),end='')
        counter +=1
        if counter > l:
            counter =0

pao()