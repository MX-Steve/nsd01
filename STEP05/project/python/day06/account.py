"""
编写记账程序
"""
import os
import time
import pickle as p


def save_money(record, wallet):
    try:
        amount = float(input('amount:'))
        comment = input('comment:')
    except :
        print("\ninvalid input")
        return
    date = time.strftime("%Y-%m-%d")

    with open(wallet, 'rb') as fobj:
        balance = p.load(fobj) + amount
    with open(wallet,'wb') as fobj:
        p.dump(balance,fobj)
    with open(record,'a') as fobj:
        fobj.write('%-15s %-15s %-8s %-8s %-20s\n'%(date,amount,'',balance,comment))


def cost_money(record, wallet):
    try:
        amount = float(input('amount:'))
        comment = input('comment:')
    except :
        print("\ninvalid input")
        return
    date = time.strftime("%Y-%m-%d")

    with open(wallet, 'rb') as fobj:
        balance = p.load(fobj) - amount
    with open(wallet, 'wb') as fobj:
        p.dump(balance, fobj)
    with open(record, 'a') as fobj:
        fobj.write('%-15s %-15s %-8s %-8s %-20s\n' % (date, '', amount, balance, comment))

def query_money(record, wallet):
    print('%-15s %-8s %-8s %-10s %-20s' % ('日期', '收入', '支出','余额', '注释'))
    with open(record,'r') as fobj:
        for line in fobj:
            print(line)
    with open(wallet,'rb') as fobj:
        print('\033[32;1mlatest balance:%d\033[0m' % p.load(fobj))

def show_menu():
    record = "record.txt"
    wallet = "wallet.data"
    if not os.path.exists(wallet):
        with open(wallet, 'wb') as fobj:
            p.dump(10000, fobj)
    cmds = {"0": save_money, '1': cost_money, '2': query_money}
    prompt = """[0]save money
[1] cost money
[2] query money
[3] quit
please input your choice[0/1/2/3]
"""
    while True:
        try:
            choice = input(prompt).strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt,EOFError):
            print('\nBye-Bye')
            choice = 3
        if choice not in '0123':
            print("invalid value")
            continue
        if choice == '3':
            break
        cmds[choice](record, wallet)


if __name__ == '__main__':
    show_menu()
