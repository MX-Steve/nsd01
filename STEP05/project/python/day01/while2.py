import random
r = random.randint(1,10)#1或10
print(r)
running = True
while running:
    an = int(input("guess the n:"))
    if an == -1:
        print("不玩了")
        running = False
    elif an < r:
        print("\033[31;1m 小了! \033[0m")
    elif an > r:
        print("\033[32;1m 大了! \033[0m")
    else:
        print("\033[33;1m 对了! \033[0m")
        running = False

