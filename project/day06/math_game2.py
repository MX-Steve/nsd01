# import random
from random import randint, choice

# def add(x,y):
#     return x+y
# def sub(x,y):
#     return x-y

def exam():
    # n1 = random.choice(range(100))
    # n2 = random.choice(range(100))
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)
    op = choice('+-')
    cmds={"+":lambda x,y:x+y,"-":lambda x,y:x-y}
    result = cmds[op](*nums)
    prompt="%s %s %s ="%(nums[0],op,nums[1])
    counter = 0
    while counter <3:
        try:
            your = int(input(prompt))
        except:
            print()
            continue
        if your == result:
            print("\033[32;1myou are right!\033[0m")
            break
        else:
            print("\033[33;1myou are wrong!\033[0m")
            counter +=1
    else:
        print("%s%s"%(prompt,result))
    # 法二：
    # if op == "+":
    #     result = nums[0] + nums[1]
    # else:
    #     result = nums[0] - nums[1]


if __name__ == '__main__':
    while True:
        exam()
        try:
            yn = input("continue?y/n?").strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            yn = 'n'
        if yn in 'Nn':
            print("\nBye-Bye")
            break
