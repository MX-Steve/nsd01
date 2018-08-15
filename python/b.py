#!/usr/local/bin/python3
i = ['a','b']
l = [1, 2]
print(dict([i,l]))

print("===========修改文件权限=============")
import os
os.chmod("a.py",0o755)
print("===========还行显示=============")
names = '''lisi
haha
xixi
hehe
heihei
'''
print(names)
print("===========定义字符串=============")
py_str = 'python'
print(len(py_str))
print(py_str[-2])
print(py_str[2:4])
print(py_str[2:])
print(py_str[:4])
print(py_str*2)
print(py_str[::2]) #2为步长值
print(py_str[1::2])#从1开始，2为步长值
print(py_str[::-1])#-1为负值，从右往左取值
print("===========定义列表=============")
alist = [1,'tom','jack',[11,22,33]]
r='tom' in alist
r1=22 in alist
r2=1 in alist
print(r2)
alist[1]="xixi"
print(alist)
print(alist[-1][1])