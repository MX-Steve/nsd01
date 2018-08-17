import datetime
import time
print(time.localtime(time.time()))

print("#######################")
#斐波那切
#0 1 1 2 3 5 8
#方法一：
a=0;b=1
while a<=10:
    print(a, b, end=" ")
    a = a + b
    b = a + b

#方法二：
fib = [0,1]
for i in range(8):
    fib.append(fib[-1]+fib[-2])
print(fib)


print("\n##################################")
print(list(range(1,10,2)))
print(list(range(10,1,-2)))

print("#################九九乘法正#################")

x=1
while x <=9:
    y=1
    while y <= x:
        s=x,"x",y,"=",x*y
        # print(len(s))
        if len(s)==5:
            print(x,"x",y,"=",x*y,end="      ")
        else:
            print(x, "x", y, "=", x * y, end=" ")
        y+=1
    x+=1
    print()
print("#################九九乘法反#################")
for i in range(10,0,-1):
    for j in range(i,0,-1):
        print(i,"x",j,"=",i*j,end="   ")
    print()


astr="abc"
alist = ['bob','alice']
atuple = (10,20,30)
adict = {"name":"tom","age":24}
a1 = {"name":"lisi","age":23,"sex":"boy","school":"danei"}
for ch in astr:
    print(ch)
for name in alist:
    print(name)
for i in atuple:
    print(i)
for key in adict:
    print("%s:%s" % (key,adict[key]))
for u in a1:
    print("%s:%s" % (u,a1[u]))

print("##############################")
#人头
i=0
print("\033[33;1m#\033[0m"*45)
while i < 20:
    j=0
    while j < 45:
        if j == 0 or j == 44:
            print("\033[33;1m#\033[0m",end="")
        #眼睛
        elif (3 <=j<=11) and (2<=i<=3) :
            print("\033[31;1m#\033[0m",end="")
        elif (11 <j<32) and i==2 :
            print(" ", end="")
        elif (32 <=j<=40) and (2<=i<=3) :
            print("\033[31;1m#\033[0m", end="")
        elif (15<=j<=30) and (i==12 or i==14):
        #嘴巴
            print("\033[32;1m#\033[0m", end="")
        elif (15<=j<=17 or 20<j<=25 or 28<=j<=30) and (i==13):
            print("\033[30;1m#\033[0m", end="")
        #鼻子
        elif (7<=i<=10) and (21<=j<=23):
            print("\033[33;1m#\033[0m", end="")
        else:
            print(" ",end="")

        j+=1
    i+=1
    print()
print("\033[33;1m#\033[0m"*45)

print("##############################")


import  random

all_choices = ['剪刀',"石头","布"]

while True:
    computer = random.choice(all_choices)
    player = int(input('''
    [0]剪刀
    [1]石头
    [2]布
    请输入：
    '''))
    player = all_choices[player]
    win_list = [["石头","剪刀"],["剪刀","布"],["布","石头"]]
    if player == computer:
        print("\033[31;1m平\033[0m")
    elif [player,computer] in win_list:
        print("赢了")
        break
    else:
        print("输了")