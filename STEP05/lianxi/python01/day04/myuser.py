#!/usr/bin/env python
"this is a file about useradd a user"

from  randpass import gen_pass
import sys
import subprocess



def add_user(user,password,fname):
    subprocess.call(
        "useradd %s " % user,
        shell= True
    )
    subprocess.call(
        "echo %s | passwd --stdin %s" % (password,user),
        shell=True
    )
    info = """username:%s ; password:%s \n""" %(user,password)
    with open(fname,'a') as fobj:
        fobj.write(info)


if __name__ == '__main__':
    username = sys.argv[1]
    password = gen_pass()
    add_user(username,password,'/tmp/a.txt')
