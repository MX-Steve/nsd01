#!/usr/bin/env python3
import os
def get_fname():
    while True:
        fname = input("input your file name: ")
        if not os.path.exists(fname) :
            break
        print("%s is already exists, please rename" % fname)
    return fname

def get_content():
    content = []
    print("input your content , end is funished! ")
    while True:
        line = input(">")
        if line == "end":
            break
        content.append(line)
    return content

def wfile(fname,content):
    with open(fname,'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ['%s\n' % line for line in content]
    wfile(fname,content)
