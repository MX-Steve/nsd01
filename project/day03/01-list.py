# [10]
# [3+2]
# a=[3+2 for i in range(10)]
# print(a)
#
# b=[3+i for i in range(10)]
# print(b)
#
# c=[3+i for i in range(10) if i%2==1]
# print(c)
#
# d=['192.168.1.%s' % i for i in range(1,255)]
# print(d)

#cp /etc/passwd /tmp/mima
fobj=open("/tmp/mima") #r方式打开
data = fobj.read()
# print(data)
# fobj.close()
f1=open("/etc/hostname")
d1=f1.read()
# print(d1)
fobj.close()
# fobj=open("/tmp/mima")
#print(fobj.read(4)) #指定读取4字节，建议4096的倍数，1block=4字节
# print(fobj.readline())
#print(fobj.readlines())#读入列表
# print(fobj.readline(4))
# print(fobj.readline(4))
# print(fobj.read(4))
# fobj.close()
fobj = open('/tmp/mima','w')
# for line in fobj:
#     # print(line,end='')
#     print(line)
# print(fobj.readline())
# print(fobj.readline())
# fobj.write("hello world \n") #内容达到一定程度时自动写入磁盘
# fobj.flush() ==>刷新后写入
fobj.writelines(['2nd line.\n','new line.\n'])
fobj.writelines(['xxxooojjj\n','oooooo\n'])
#fobj.close() #==>关闭后写入
fobj.write('ssdfsderesxeeee\nfsetgsaf\n')