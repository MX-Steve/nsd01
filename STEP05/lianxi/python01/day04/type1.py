# list('abcd')
# list(('a','b'))
# tuple('abcd')
# tuple(['a','b'])


# from random import randint
# alist = [randint(1,100) for i in range(10)]
# print(max(alist))
# print(min(alist))

# alist = ['zhangsan','lisi','wangwu']
# for ind in range(len(alist)):
#     print("%s : %s " %(ind,alist[ind]))
#
# for item in enumerate(alist):
#     print("%s : %s "%(item[0],item[1]))
#
# for ind,val in enumerate(alist):
#     print("%s : %s " %(ind, val))
#
# print(list(reversed(alist)))
#
# print(sorted(alist))

a = 'lllL'
b = a.encode('utf8')
print(b)
c = b.decode('utf8')
print(c)