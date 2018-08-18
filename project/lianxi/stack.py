#!/usr/bin/env python3
stack=[]
def push_it():
  ch=input("输入内容：")
  stack.append(ch)
  #print('push')
def pop_it():
  if stack:
    stack.pop()
  #print('pop')
def view_it():
  print(stack)
  #print('view')
def show_menu():
  choice={"0":push_it,"1":pop_it,"2":view_it}
  mes="""请选择：
[0] push_it()
[1] pop_it()
[2] view_it()
[3] quit
input:0/1/2/3
"""
  while True:
    num = input(mes).strip()[0]
    if num not in "0123":
      print("Invalid number")
      continue
    if num == '3':
      break
    choice[num]()

if __name__=="__main__":
  show_menu()
