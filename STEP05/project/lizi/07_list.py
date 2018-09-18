#!/usr/bin/env python3
"""
列表也是序列对象，但它是容器类型，列表中可以包含各种各样的数据
"""
alist = [1,2,3,'bob',[10,20,30]]
print(len(alist))
alist[-1]
alist[-1][-1]
print([1,2,3][-1])
print(10 in alist)
print('o' in alist)
alist[-1] = 100
alist.append(200)
print(alist)
