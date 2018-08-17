#!/usr/local/bin/python3
# a,b = 45,23
# s = a if a <5 else b
# print(s)
import random
jiqi = random.randint(1,3)
you = input("请输入：剪刀石头布")
if jiqi == 1:
    jiqi = "剪刀"
elif jiqi == 2:
    jiqi = "石头"
elif jiqi == 3:
    jiqi = "布"

if you == "剪刀":
    if jiqi == "剪刀":
        print("平局")
    elif jiqi == "石头":
        print("输了")
    else:
        print("赢了")
elif you == "石头":
    if jiqi == "剪刀":
        print("赢了")
    elif jiqi == "石头":
        print("平局")
    else:
        print("输了")
else:
    if jiqi == "剪刀":
        print("输了")
    elif jiqi == "石头":
        print("赢了")
    else:
        print("平局")
print("jiqi:",jiqi)