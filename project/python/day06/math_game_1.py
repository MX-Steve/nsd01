#!/usr/bin/env python3
from random import randint, choice


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def math():
    nums=[randint(1,100) for i in range(2)]
    nums.sort(reverse=True)
    op=choice('+-')
    cmds = {"+":add,"-":sub}
    result=cmds[op](*nums)
    prompt="%s %s %s ="%(nums[0],op,nums[1])
    counter = 0
    while counter < 3:
        try:
            your = int(input(prompt))
        except:
            print()
            continue
        if your == result:
            print("wright!")
            break
        else:
            print("wrong!")
            counter +=1
    else:
        print("正确答案为：")
        print("%s %s" % (prompt,result))


if __name__ == '__main__':
    while True:
        math()
        prompt = "continue?y/n"
        try:
            yn = input(prompt).strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        if yn in 'Nn':
            print("\nBye-Bye")
            break
        else:
            continue

