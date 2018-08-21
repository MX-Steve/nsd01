import time

result=0

start = time.time()
for i in range(1,20000000):
    result +=1

end=time.time()
print(result,end-start)