#!/usr/bin/env python3
"""
元组练习
"""
print(list('abcd'))
print(list((10,20,30)))
print(tuple('abcd'))
print(str(100))
print(str((10,20,30)))
print(max([1,4,3,10,2]))
print(min([10,4,12,3,10,2]))
print(max('hello'))

users = ['bob','alice','john']
for i in range(len(users)):
  print("#%s:%s"%(i,users[i]))

print(list(enumerate(users)))
print(enumerate(users))
for i,v in enumerate(users):
  print("#%s:%s"%(i,v))

for u in reversed(users):
  print(u)

sorted(users)
