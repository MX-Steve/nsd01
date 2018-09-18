#!/usr/bin/env python3
alist=[1,40,50,100]
alist[0]=10
alist[1:3]=[2,3,4,5]
alist[3:3]=[50,60]
alist.sort()
alist.reverse()
alist.count(10)
alist.append(50)
alist.append(60)
#alist.extend('abc')
ind=alist.index(50)
print(ind)
alist.insert(2,1000)




print(alist)
