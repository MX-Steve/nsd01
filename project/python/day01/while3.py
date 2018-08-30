# while True:
#     yn = input("continue...?")
#     if yn in ['n','N']:
#         break
#     else:
#         print("running")

while True:
    yn = input("continue...?")
    if yn in ['n','N']:
        break
    print("running")

import random
r = random.randint(1,10)#1或10
print(r)
running = True
counter = 0
while counter < 3:
    counter += 1
    an = int(input("guess the n:"))
    if an == -1:
        print("不玩了")
        break
    elif an < r:
        print("\033[31;1m 小了! \033[0m")
    elif an > r:
        print("\033[32;1m 大了! \033[0m")
    else:
        print("\033[33;1m 对了! \033[0m")
        break
else:
    print("Low Bee")

