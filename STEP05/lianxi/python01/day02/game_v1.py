import random
"""
a:jiandao
b:shitou
c:bu
"""
jiqi = random.choice(["a",'b','c'])
win = [['a','c'],['b','a'],['c','b']]
you = input("chu:")
print("you are %s, computer is %s"%(you,jiqi))
if jiqi == you:
    print("ping")
elif [you,jiqi] in win :
    print("\033[31;1mwin\033[0m")
else:
    print("\033[32;1mlose\033[0m")