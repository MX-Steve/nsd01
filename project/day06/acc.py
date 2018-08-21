#!/usr/bin/env python3
"""
模拟收入支出
"""
import os
import time
import pickle as p

def save_money(rec,w):
    try:

        comment = input("comment:")
        account=float(input("account:"))
    except:
        print('invalid value')
        return
    date = time.strftime("%Y-%m-%d")
    with open(w,'rb') as fobj:
        balance = p.load(fobj) + account
    with open(w,'wb') as fobj:
        p.dump(balance,fobj)
    with open(rec,'a') as fobj:
        fobj.write("\n%-10s %-10s %-10s %-10s %-10s"%(date,account,'',balance,comment))

def cost_money(rec,w):
    try:

        comment = input("comment:")
        account = float(input("account:"))
    except:
        print('invalid value')
        return
    date = time.strftime("%Y-%m-%d")
    with open(w, 'rb') as fobj:
        balance = p.load(fobj) - account
    with open(w, 'wb') as fobj:
        p.dump(balance, fobj)
    with open(rec, 'a') as fobj:
        fobj.write("\n%-10s %-10s %-10s %-10s %-10s" % (date, '',account, balance, comment))

def query_money(rec,w):
    print("\n%-10s %-10s %-10s %-10s %-10s" % ('date', 'get','out', 'balance', 'comment'))
    with open(rec,'r') as fobj:
        for line in fobj:
            print(line,end='')
    with open(w,'rb') as fobj:
        print("\nlatest money:%s"% p.load(fobj))


def show_menu():
    prompt = """[0] save money
    [1] cost money
    [2] query money
    [3] quit    
    """
    rec = 'rec.txt'
    w = 'w.data'
    cmds = {"0":save_money,"1":cost_money,"2":query_money}
    if not os.path.exists(w):
        with open(w, 'wb') as fobj:
            p.dump(10000, fobj)
    while True:
        try:
            choice = input(prompt).strip()[0]
        except IndexError:
            print("invalid value")
            continue
        except (KeyboardInterrupt,EOFError):
            choice='3'
        if choice not in '0123':
            print("input value error")
        if choice == '3':
            print("\nBye-Bye")
            break
        cmds[choice](rec,w)


if __name__ == '__main__':
    show_menu()