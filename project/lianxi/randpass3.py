#!/usr/bin/env python3
"""
随机生成验证码，位数默认6位
"""
from random import choice
from string import ascii_letters,digits

all_chs = ascii_letters + digits

def randpass(n=6):
  result=''
  for i in range(n):
    result += choice(all_chs)
  return result

if __name__=="__main__":
  print(randpass())
  print(randpass(10))
