def func1(*args):
    print(args) # 标示args是个元组

def func2(**kwargs):
    print(kwargs)

def func3(*args,**kwargs):
    print(args)
    print(kwargs)
    #pass

def f1(*args,**kwargs):
    print(args)
    print(kwargs)

def add(x,y):
    print(x+y)

def get_info(name,age):
    print("%s is %s years old"%(name,age))


if __name__ == '__main__':
    f1(111,'123','adf',name="tom")
    func1()
    func1('hao')
    func1('hao',234)
    func1('hao',2122,'wolrd')

    func2(name="zhangsan")
    func2(name="zhangsan",age=24)

    func3(10,'hello',name='bob',age=21)
    nums = [10,5]
    add(nums[0],nums[1])
    add(*nums)#将元组拆开

    get_info(age=23,name='alice')
    user={"name":"alice","age":24}
    get_info(**user) #将字典拆开t=v