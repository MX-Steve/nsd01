import shutil


# f1 = open('/etc/hosts', 'rb')
# f2 = open('/tmp/zhuji', 'wb')
# shutil.copyfileobj(f1,f2)
# f1.close()
# f2.close()


# shutil.copyfile('/etc/hosts','/tmp/zj')
# shutil.copy2('/etc/hosts' , '/tmp')
# shutil.move('/tmp/passwd', '/tmp')
# shutil.rmtree('/tmp/hosts')

# shutil.chown('/tmp/ls',user='zhangsan',group='zhangsan')

a,b = 10, 20
(a,b)=(b,a)

print(a,b)
a, b = b, a
print(a,b)

a,b = [10,20]
print(a,b)