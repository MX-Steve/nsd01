# 随机数
from random import choice

import string

# from string import ascii_letters, digits

# 对于不改变的常量放在外面
all = 'abcdefghijklmnopqrstuvwxyz0123456789QWERTYUIOPASDFGHJKLZXCVBNM'
#all = ascii_letters + digits

def randpass(n=8):
    result = [choice(all) for i in range(n)]
    return ''.join(result)
    # 将列表的字符集用空字符串拼接起来


if __name__ == '__main__':
    print(randpass())
