with open("/tmp/mima") as fobj:
    fobj.readline()

fobj = open('/tmp/mima','rb')#b:字节类型
fobj.tell()
fobj.seek(10,0)
'''
seek第二个参数：
    0:从头开始
    1:从当前位置开始
    2:从文章结尾开始
'''
'''
seek 和 sys
fobj.read(4)
fobj.seek(-5,2) #移动到文件倒数第五个字节,只有rb支持倒着来

import sys
a=sys.stdin.readline()#读取键盘输入，回车也作为一个字符读入
print(a)
# sys.stdout.write(a)
print(len(a))
'''
