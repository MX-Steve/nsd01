from random import choice
from string import ascii_letters, digits


all = ascii_letters + digits

def ra(n=8):
    result = [choice(all) for i in range(n)]
    return ''.join(result)


if __name__ == '__main__':
    ra()
