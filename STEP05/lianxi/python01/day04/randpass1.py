from random import choice
from string import ascii_letters, digits
pool = ascii_letters + digits

def gen_pass(n=8):

    result = ''
    for i in range(n):
        ch = choice(pool)
        result += ch
    return result


if __name__ == "__main__":
    print(gen_pass())
    print(gen_pass(4))

