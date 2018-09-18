#!/usr/bin/env python3
"""
该脚本是用来创建用户，设置随机密码
用户登录后，让用户修改密码
"""
from randpass import randpass
import sys
import subprocess

def adduser(username,password,filename):
  user_info = """user infomation
用户名：%s
密码：%s
"""%(username,password)
  subprocess.call('useradd %s'%username,shell=True)
  subprocess.call(
    'echo %s | passwd --stdin %s'%(password,username),
    shell=True
  )
  with open(filename,'a') as fobj:
    fobj.write(user_info)


if __name__=="__main__":
  username=sys.argv[1]
  password=randpass()
  adduser(username,password,"/tmp/a.txt")
