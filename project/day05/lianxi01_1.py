#!/usr/bin/env python3
"""
模拟用户登录注册
"""
userdb={}
def login():
    user=input("user:")
    passwd=input("pass:")
    if userdb[user]==passwd:
        print("login ok")
    else:
        print("login err")

def register():
    user=input("user:")
    if user not in userdb:
        passwd=input("pass:")
        userdb[user]=passwd
    else:
        print("用户名已经存在")

def show_menu():
    cmds={"0":register,"1":login}
    info = """login/register
[0] register
[1] login
[2] exit
请选择[0/1/2]    
"""
    while True:
        choice=input(info).strip()[0]
        if choice not in "012":
            print("input err")
            continue
        if choice == '2':
            break
        cmds[choice]()


if __name__ == '__main__':
    show_menu()