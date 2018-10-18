def randpass(n=8):
    from random import choice
    pool='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    result = ''
    for i in range(n):
        ch=choice(pool)
        result +=ch

    print(result)

n = 6
randpass(n)