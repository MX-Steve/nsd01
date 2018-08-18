#/usr/local/bin/python3
import sys,re

def configip(fname,ip_addr,if_ind):
    content = '''TYPE=Ethernet
BOOTPROTO=none
NAME=eth%s
DEVICE=eth%s
ONBOOT=yes
IPADDR=%s
PREFIX=24
''' % (if_ind,if_ind,ip_addr)
    with open(fname,'w') as fobj:
        fobj.write(content)

def check_ip(ip_addr):
    m = re.match(r'(\d{1,3}\.){3}\d{1,3}$',ip_addr)
    if not m:
        return False
    return True

def show_menu():
    prompt = '''configure IP Address:
(0) eth0
(1) eth1
(2) eth2
(3) eth3
Your choice(0/1/2/3):'''
    try:
        if_ind = input(prompt).strip()[0]
    except:
        print("IP error!")
        sys.exit(1)

    if if_ind not in "0123":
        print("wrong selection.")
        sys.exit(2)













