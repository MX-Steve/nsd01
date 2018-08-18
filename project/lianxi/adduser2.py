#!/usr/bin/env python3
"""
创建用户，设置随机密码，并将用户信息存到一个文件里
"""
import sys
from randpass import randpass 
import subprocess

def adduser(username,password,filename):
  user_info ="""user infomation
用户名：%s
密码：%s
"""  %(username,password)
  subprocess.call('useradd %s'%username,shell=True)
  subprocess.call('echo %s|passwd --stdin %s'%(password,username),shell=True)
  with open(filename,'a') as fobj:
    fobj.write(user_info)


if __name__=="__main__":
  if len(sys.argv)==2:
    username=sys.argv[1]
    password=randpass(6)
    adduser(username,password,"/tmp/user.txt")
  else:
    print("您需要将用户名写在脚本后面")
