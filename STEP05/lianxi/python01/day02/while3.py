import random
"""
a:jiandao
b:shitou
c:bu
"""

win = [['a','c'],['b','a'],['c','b']]
run = True
while run:
    jiqi = random.choice(["a", 'b', 'c'])
    you = input("chu:")
    if you == "exit":
        print("bye")
        run = False
    print("you are %s, computer is %s"%(you,jiqi))
    if jiqi == you:
        print("ping")
    elif [you,jiqi] in win :
        print("\033[31;1mwin\033[0m")
        run = False
    else:
        print("\033[32;1mlose\033[0m")