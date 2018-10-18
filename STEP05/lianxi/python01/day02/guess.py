import random

rn = random.randint(1, 5)
#print(rn)
answer = int(input("guess a number:"))
if answer > rn :
    print("bigger then the num")
elif answer < rn :
    print("smaller than the num")
else:
    print("you are right!")

