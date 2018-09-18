#集合： 像一个无值的字典{}
# s1 = set('hello')
# print(s1)
# print(len(s1))
# for ch in s1:
#     print(ch)
# print('o' in s1)
# s2 = frozenset('hello')
# print(s2)
# a1={'a','b','c'}
# a2={'b','c','d'}
# print(a1 | a2)
# print(a1 & a2)
# s1.add(10)
# print(s1)
# s1.update(['hello','world'])
# s1.remove(10)
# print(s1)
s1 = set('hello')
print(len(s1))
s2 = frozenset('hello')
for i in s1:
    print(i)
s3 = {'e','o','a'}
print(s1 | s3)
print(s1 & s3)
s3.add('lili')
s3.update(['haha','xixi'])
s3.remove('o')
print(s3)
s4 = {'a','e'}
print(s4.issubset(s3))
print(s3.issuperset(s4))
s1.union(s2) #s1 | s2
s1.intersection(s2) # s1 & s2
s1.difference(s2) # s1-s2