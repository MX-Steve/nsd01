#!/usr/bin/env python3
"""
模拟钱包
"""
import os
import time
import pickle as p


def save_money(qianbao,tongji):
    date = time.strftime("%Y-%m-%d")
    try:
        account=float(input("account:"))
        comment=input("comment:")
    except:
        print("input error")
        return
    with open(qianbao,'rb') as fobj:
        yue=p.load(fobj) + account
    with open(qianbao,'wb') as fobj:
        p.dump(yue,fobj)
    with open(tongji,'a') as fobj:
        fobj.write('%-10s %-10s %-10s %-10s %-10s\n'%(date,account,'',yue,comment))

def cost_money(qianbao,tongji):
    date = time.strftime("%Y-%m-%d")
    try:
        account = float(input("account:"))
        comment=input("comment:")
    except:
        print("input error")
        return
    with open(qianbao,'rb') as fobj:
        yue = p.load(fobj) - account
    with open(qianbao,'wb') as fobj:
        p.dump(yue,fobj)
    with open(tongji,'a') as fobj:
        fobj.write('%-10s %-10s %-10s %-10s %-10s\n'%(date,'',account,yue,comment))

def query_money(qianbao,tongji):
    print('%-10s %-10s %-10s %-10s %-10s\n'%('date','add','reduce','yue','comment'))
    with open(tongji,'r') as fobj:
        for line in fobj:
            print(line,end='')
    with open(qianbao,'rb') as fobj:
        print("\033[33;1mlastest money : %s\033[0m" % p.load(fobj))


def show_menu():
    qianbao="qianbao.data"
    tongji="tongji.txt"
    if not os.path.exists(qianbao):
        with open(qianbao,'wb') as fobj:
            p.dump(10000,fobj)

    prompt = """[0] save_money
[1] cost_money
[2] query_money
[3] exit"""
    cmds = {"0": save_money, "1": cost_money, "2": query_money}
    while True:
        try:
            choice = input(prompt).strip()[0]
        except IndexError:
            print("invalid value")
            continue
        except (KeyboardInterrupt, EOFError):
            choice = '3'
        if choice not in '0123':
            print('invalid value')
        if choice == '3':
            break
        cmds[choice](qianbao,tongji)

if __name__ == '__main__':
    show_menu()
