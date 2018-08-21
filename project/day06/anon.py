from random import randint
def add(x,y):
    return  x+y

def func1(x):
    return x%2
def func2(x):
    return x*2 +1

if __name__ == '__main__':
    # print(add(10,5))
    # a = lambda x,y:x+y
    # print(a(10,5))
    nums = [randint(1,100) for i in range(10)]
    print(nums)
    #filter的第一个参数是函数，这种被称作高阶函数，把第二个参数一个一个传入第一个函数
    print(list(filter(func1,nums)))
    print(list(filter(lambda x:x%2,nums)))
    print(list(map(func2,nums)))
    print(list(map(lambda x:x*2+1,nums)))
    print(list(map(lambda x:x*2,[num for num in range(10)])))