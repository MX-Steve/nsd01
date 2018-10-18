import random
"""
a:jiandao
b:shitou
c:bu
"""
jiqi = random.choice(["a",'b','c'])
win = [['a','c'],['b','a'],['c','b']]
while 1:
    you = input("chu:")
    if you == "exit":
        print("bye")
        exit(1)
    print("you are %s, computer is %s"%(you,jiqi))
    if jiqi == you:
        print("ping")
    elif [you,jiqi] in win :
        print("\033[31;1mwin\033[0m")
        exit(2)
    else:
        print("\033[32;1mlose\033[0m")