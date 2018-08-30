def foo():
    print('in foo')
    bar()

def  bar():
    print("in bar")

def get_info(name,age):
    print("%s is %s year old"%(name,age))

if __name__ == '__main__':
    # foo()
    get_info('bob',25)
    get_info(age=25,name='bob') #key=value的形式必须出现在后面
    # get_info(25,name="bob") error
    get_info('bob',age=24)