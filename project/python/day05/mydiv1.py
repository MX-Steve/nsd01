# try:
#     f1=open("/tmp/users.txt",'w')
# except  FileNotFoundError:
#     print("No such file")
# else:
#     f1.writelines('xixix\n')
# finally:
#     f1.close()
# print("down")
def set_age(name,age):
    if not 0<age<120:
        raise ValueError("年龄异常")
    print("%s is %s years old"%(name,age))

def set_age2(name,age):
    assert 0<age<120, '年龄异常'
    print("%s is %s years old"%(name,age))

def set_age3(name,age):
    if not 0<age<120:
        raise ValueError("年龄异常")
    print("#%s:%s",(name,age))

if __name__ == '__main__':
    set_age('bob',20)
    set_age2('tom',20)