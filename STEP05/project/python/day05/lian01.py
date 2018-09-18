#!/usr/bin/env python
"""
模拟用户登录信息系统
"""
from getpass import getpass
userdict={}
def register():
    username=input("user:")
    if username not in userdict:
        password = input("passwd:")
        userdict[username]=password
    else:
        print("%s已存在"%username)

def login():
    username=input('user:')
    password=getpass('passwd:')
    if userdict.get(username) !=password:
        print("登录失败")
    else:
        print("登录成功")


def show_menu():
    cmds={"0":register,"1":login}
    info = """menu list
    [0] register
    [1] login
    [2] exit
    请选择:[0/1/2]
        """
    while True:
        choice=input(info).strip()[0]
        if choice not in "012":
            print("无效选择")
            continue
        if choice == "2":
            break
        cmds[choice]()


if __name__ == '__main__':
    show_menu()