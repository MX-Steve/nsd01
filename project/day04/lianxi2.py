#!/usr/bin/env python3
"""
1.创建文件,不存在则创建,并写入内容,存在,则重新创建
"""
import os

def get_fname():
    while True:
        fname = input("filename:")
        if not os.path.exists(fname):
            break
        print("%s already exits,try again" % fname)
    return fname

def get_content():
    content = []
    print("input context:end is end!")
    while True:
        line = input(">")
        if line == "end":
            break
        content.append(line)
    return content

def create_file(fname,content):
    with open(fname,'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ["%s\n" % line for line in content]
    create_file(fname,content)