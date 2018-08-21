"""
阶乘：5!=5*4*3*2*1
5!=5*4!
4!=4*3!
"""


def func(x):
    if x == 1:
        return 1
    return x * func(x - 1)

if __name__ == '__main__':
    print(func(5))
    print(func(6))
