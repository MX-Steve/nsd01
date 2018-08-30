#!/usr/bin/env python3
import sys
import subprocess
from randpass import randpass


def adduser(username, password, fname):
    subprocess.call(
        "useradd %s" % username, shell=True
    )
    subprocess.call(
        "echo %s | passwd --stdin %s" % (password, username), shell=True
    )
    user_info = """user information
username:%s
password:%s""" % (username, password)

    with open(fname, 'a') as fobj:
        fobj.write(user_info)


if __name__ == '__main__':
    username = sys.argv[1]
    # password = "12345678"
    password = randpass()
    adduser(username, password, '/tmp/users.txt')
