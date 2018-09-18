#!/usr/local/bin/python3
import  getpass
name = input("请输入姓名：")
pw = getpass.getpass("password：")
if name == "bob":
    if pw == "123456":
        print('\033[32;5m Login successful\033[0m')
    else:
        print('\033[31;4m PW err \033[0m')
else:
    print('\033[31;5m name err \033[0m')

