#!/usr/bin/env python3
"""
1.创建文件名，如果存在，则换一个名字
2.创建需要录入的内容
3.写入文件
"""
import os

def getfile():
  while True:
    fname=input("请输入文件名：")
    if os.path.exists(fname):
      print("%s已经存在，请重试：" % fname)
    else:
      break
  return fname

def getcontent():
  print("请输入正文：end表示结束")
  content=[]
  while True:
    line=input(">")
    if line == "end":
      break
    content.append(line)
  return content

def wfile(fname,content):
  with open(fname,'w') as fobj:
    fobj.writelines(content) 

if __name__=="__main__":
  fname=getfile()
  content=getcontent()
  content=['%s\n' % line for line in content]
  wfile(fname,content)




