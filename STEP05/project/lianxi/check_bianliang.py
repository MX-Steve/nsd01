#!/usr/bin/env python3
"""
判断变量是否合法
"""
from string import ascii_letters,digits
from keyword import iskeyword
first_letter=ascii_letters + "_"
other_letters=first_letter + digits

def check_var(var):
  if iskeyword(var):
    return "%s是关键字" % var
  if var[0] not in first_letter:
    return "%s首字母不合法" % var
  for ind,ch in enumerate(var[1:]):
    if ch not in other_letters:
      return "第%s位不合法" %(ind+2)
  return "%s是合法的" % var


if __name__=="__main__":
  var=input("input yours:")
  print(check_var(var))
