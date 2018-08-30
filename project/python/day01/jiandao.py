#!/usr/local/bin/python3
import random
'''
computer = random.choice(['剪刀',"石头","布"])
player = input("请出拳：/剪刀/石头/布")
'''
'''
if player == "剪刀":
    if computer == "剪刀":
        print("平")
    elif computer == "石头":
        print("输了")
    else:
        print("赢了")
elif player == "石头":
    if computer == "剪刀":
        print("赢了")
    elif computer == "石头":
        print("平")
    else:
        print("输了")
else:
    if computer == "剪刀":
        print("输了")
    elif computer == "石头":
        print("赢了")
    else:
        print("平")
'''
'''
if computer == player:
    print("平")
else:
    if computer == "剪刀":
        r = "赢了" if player == "石头" else "输了"
    elif computer == "石头":
        r = "赢了" if player == "布" else "输了"
    else:
        r = "赢了" if player == "剪刀" else "输了"
'''
all_choices = ['剪刀',"石头","布"]
computer = random.choice(all_choices)
player = int(input('''
[0]剪刀
[1]石头
[2]布
请输入：
'''))
player = all_choices[player]
win_list = [["石头","剪刀"],["剪刀","布"],["布","石头"]]
if player == computer:
    print("\033[31;1m平\033[0m")
elif [player,computer] in win_list:
    print("赢了")
else:
    print("输了")
























