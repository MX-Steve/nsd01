#!/usr/bin/env python3
"""
这是一个创建用户的脚本
创建用户，设置密码，并把用户信息记录到指定文件
sys模块：获取位置参数
subprocess模块：调用shell解释器
"""
from randpass import randpass
import sys
import subprocess

def adduser(username,password,filename):
  user_info = '''user information:
用户名：%s
密码：%s
'''%(username,password)
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
