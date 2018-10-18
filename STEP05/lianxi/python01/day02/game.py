import random
jiqi = random.choice(['shitou','bu','jian'])
user = input("chu: ")
if user == jiqi:
    print("ping")
else:
    if user == "shitou":
        if jiqi == "bu":
            print("shu")
        else:
            print("ying")
    elif user == "bu" :
        if jiqi == "jian":
            print("shu")
        else:
            print("ying")
    else:
        if jiqi == "bu":
            print("shu")
        else:
            print("ying")

print(jiqi)
