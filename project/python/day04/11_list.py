alist = [1, 20, 30, 45]
alist[1:3] = [40, 50, 80]

# alist[3:3] = [1,2,3,4,5,6,7,8,9]
alist[-1] = 100
alist.sort()  # 小到大
alist.reverse()  # 反序
alist.append(12)  # 追加
alist.remove(12)  # 移初
alist.extend('abc')  # 'abc'分开加入
alist.extend(['a', 'sdfs'])
alist.count(12)  # 有几个12
alist.pop()  # 弹出
alist.pop(2)  # 弹出下标为2的值
alist.index(12)  # 返回某个值的下标
alist.insert(3, 111)  # 在下标为3的位置插入

print(alist)
