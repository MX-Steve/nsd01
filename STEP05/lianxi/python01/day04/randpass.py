def gen_pass(n=8):
    from random import choice
    pool = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    result = ''
    for i in range(n):
        ch = choice(pool)
        result += ch
    return result


if __name__ == "__main__":
    print(gen_pass())
    print(gen_pass(4))

