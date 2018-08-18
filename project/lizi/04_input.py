#!/usr/bin/env python3
"""
input用法：获取用户键盘输入
注意：输入的所有内容都是字符串
"""
number = input("请输入一个数字")
print(number)
print(type(number))
#print(number + 10) 类型不一致，会报错
print(int(number)+10)
