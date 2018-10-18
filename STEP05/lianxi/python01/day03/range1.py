
for i in range(1,10,2):
    print(i)

for i in range(10,0,-2):
    print(i)

print("#" *20)

adict = ['bb','cc','aa']
for ind in range(len(adict)):
    print("%s : %s " %(ind,adict[ind]))

a=0
b=1
while a <10:
    print(a,b,end=' ')
    a=a+b
    b=a+b

fib = [0,1]
for i in range(8):
    fib.append(fib[-1]+fib[-2])
print(fib)