#列表
adict=dict(['ab','cd',('name','zhangsan')])
print(adict)
a=dict(['ab','df'])
print(a)
b={}.fromkeys(['bob','alice','tom'],7)
print(b)
for key in b:
    print('%s:%s'%(key,b[key]))

print("%(bob)s"%b)
print("%(alice)s"%b)  #==>取出健所对应的值
print(b.pop('alice'))
print('tom' in b)

c={}.fromkeys(['aaa','bbb','ccc'],['dss','123','sdfd'])
print(c)
d=b.copy()#开辟新空间
print(id(b),id(d))
print(d)
print(d.get('bob'))
print(d.get('xixi'))

mya={"name":"xixi","age":28}
print(mya.get('name'))

myb=mya.copy()
print(id(myb),id(mya))
myb.setdefault('name','haha')
print(myb)
myb.setdefault('school','danei')
print(myb)
print(myb.keys())
print(myb.values())
print(myb.items())
print(myb.update(['ss','aa']))
print(myb.update([('s',"tixi")]))
print(myb)
for key in myb.keys():
    print(key)
#哈希hash
#字典用法
#创建字典
myc={"name":"lisi","age":25}
myd={}.fromkeys(['name','age'],28)
#便利字典
#获取字典的键和值
print(myc.keys())
print(myc.values())
print(myc.items())
#更新键值
print(myc.update([('school','jinshan')]))
print(myc)
myc.setdefault('school','shandong')
myc.setdefault('home','lianyungang')
print(myc)