def foo1():
    print("hello!")

# foo1()

def foo2():
    x=1
    while x <=9:
        y=1
        while y <= x:
            s=x,"x",y,"=",x*y
            # print(len(s))
            if len(s)==5:
                print(x,"x",y,"=",x*y,end="      ")
            else:
                print(x, "x", y, "=", x * y, end=" ")
            y+=1
        x+=1
        print()

# foo2()

def foo3():
    import getpass
    uname=input("请输入用户名：")
    upass=getpass.getpass("请输入密码：")
    if uname == "li" and upass == "123":
        print("\033[32;1mwelcome\033[0m")
    else:
        print("\033[31;1muname or upass err!\033[0m")

# foo3()

def foo4(n1,n2):
    return n1+n2

# print(foo4(5,7))

def foo5(n):
    for i in range(n+1):
        for j in range(i):
            print("#",end="")
        print()

# foo5(5)

def foo6(m):
    fib=[0,1]
    for i in range(m-len(fib)):
        fib.append(fib[-1]+fib[-2])
    return fib

# f=foo6(4)
# print(f)

def foo7():
    import time
    i=0
    while True:
        print(i)
        time.sleep(1)
        i+=1
        if i >=10:
            break


# foo7()

def foo8():
    import time
    i=0
    while True:
        print("\033[31;1m       ||     ||\033[0m")
        time.sleep(1)
        i+=1
        if i >= 10:
            break

# foo8()

def foo9():
    import time,os
    t = os.system('clear')
    i=0
    while True:
        print("#")
        time.sleep(1)
        i+=1
        if i>=10:
            break

# foo9()

def foo10():
    import time,os
    t = os.system('clear')
    user_obj = open("/root/project/day03/user", 'r')
    while True:
        user=user_obj.readline()
        print("\033[32;1m",user,"\033[0m",end='')
        time.sleep(0.2)
        t = os.system('clear')
        if not user:
            foo10()


# foo10()

# import sys
# print(sys.argv)
def foo11():
    import sys
    sf = sys.argv[1]
    df = sys.argv[2]
    sf_obj = open(sf,'rb')
    df_obj = open(df,'wb')
    while True:
        data = sf_obj.read(4096)
        df_obj.write(data)
        if not data:
            break
    df_obj.close()
    sf_obj.close()

def pstar(n=20):
    print("*"*n)
pstar(3)

def pstar1():
    import time
    while True:
        print("\033[32;1m#\033[0m",end="")
        time.sleep(1)
# pstar1()