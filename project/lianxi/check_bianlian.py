#!/usr/bin/env python3
"""
判断变量是否合法的脚本
"""
from keyword import iskeyword
from string import ascii_letters,digits
first_letter = ascii_letters + '_'
other_letters = first_letter + digits

def check_bianliang(bianliang):
  #检查是否是关键字
  if iskeyword(bianliang):
    return "变量%s不能是关键词"%bianliang
  #检查变量第一位是否合法：只能是字母和下划线
  if bianliang[0] not in first_letter:
    return "变量名只能以字母或下划线开始"
  #检查其他位置是否合法
  for ind,ch in enumerate(bianliang[1:]):
    if ch not in other_letters:
      return "第%s位不合法" % (ind+2)

  return "%s是合法的" % bianliang

if __name__=="__main__":
  bianliang=input("请输入你要判断的变量名：")
  print(check_bianliang(bianliang))
