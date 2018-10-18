import getpass
user=input("input your name:\n")
passwd = getpass.getpass("input your passwd:\n")
if user == "lisi" and passwd=="123456":
    print("login successful")
else:
    print("login error")