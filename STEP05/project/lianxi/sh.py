import shutil

f1 = open('/etc/passwd', 'rb')
f2 = open('/tmp/abcd', 'wb')
shutil.copyfileobj(f1, f2)
f1.close()
f2.close()
