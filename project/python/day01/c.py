#!/usr/local/bin/python3
x,y = 7,4
print(x)
smaller = x if x < y else y
print(smaller)
print("=====score========")
score = int(input("输入成绩"))
if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
else:
    print("fail")

print("===========game：石头=============")
import random
r = random.randint(1,10)#1或10
an = int(input("guess the n:"))
if an < r:
    print("\033[31;1m 小了! \033[0m")
elif an > r:
    print("\033[32;1m 大了! \033[0m")
else:
    print("\033[33;1m 对了! \033[0m")

print(r)