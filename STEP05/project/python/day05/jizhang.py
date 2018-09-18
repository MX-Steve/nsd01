#!/usr/bin/env python3
"""
记账系统
"""
import time
def shouru():
    #时间,余额
    ru=int(input("收入金额:"))
    with open('/root/project/day05/qianbao.txt','rb')  as fobj:
        yue=int(fobj.read())+ru
    mytime = time.localtime()
    print("%s-%s-%s"&(mytime.tm_year,mytime.tm_mon,mytime.tm_mday))
    # zhangdan_list="%-10s %-10s %-10s %-10s %s"%(mytime,ru,0,yue,shuoming)
    # with open('zhangdan.txt','wb') as fobj:
    #     fobj.writelines(zhangdan_list)

def zhichu():
    print("zhichu")

def chakan():
    print("chakan")

def menu_list():
    mscmd={"0":shouru,"1":zhichu,"2":chakan}
    info="""收入指出软件
[0] shouru
[1] zhichu
[2] chakan
"""
    choice=input(info).strip()[0]
    if choice not in '0/1/2':
        print("value error!")
        exit(1)
    mscmd[choice]()

if __name__ == '__main__':
    menu_list()