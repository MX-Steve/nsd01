#192.168.1.1  mac地址
import re
print(re.match('f..','food'))
print(re.match('f..','seafood')) # match 从开头匹配
m=re.search('f..','seafood') #从任意位置匹配
print(re.search('^f..','seafood'))

print(m.group()) #返回匹配到的值
re.findall('f..','seafood is food') #返回list匹配列表
n=re.finditer('f..','seafood is food') #返回的是对象
#返回由匹配对象构成的迭代器,迭代器中的每个对象都有group方法
for m in n:
    print(m.group())
a=re.split('-|\.','hello-word-aaa.tar.gz')
print(a)
b=re.sub('X','zzg','hi X. How are you, X?') #把最后字符串中的X替换成zzg
print(b)
patt = re.compile('f..')


