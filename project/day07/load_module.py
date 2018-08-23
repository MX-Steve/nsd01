# 导入模块，site-packages ,自己的模块放在这个目录里
# 还可以设置环境变量 PYTHONPATH，指向自己所写模块的路径
# 如果一个模块文件在一个目录中，可以把目录当作包
# mkdir rrr
# cp railway rrr/
# >>> import rrr.railway
# md5值
import hashlib
with open('/tmp/passwd','rb') as fobj:
    data = fobj.read()

m = hashlib.md5(data)
print(m.hexdigest())