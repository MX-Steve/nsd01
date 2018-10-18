#!/usr/bin/env python3
"this is a touch file python "
import os

def get_fname():
    while True:
        fname = input("wenjian: ")
        if not os.path.exists(fname):
            break
        print("%s already exists, please again !" % fname)
    return fname


def get_content():
    content = []
    print("input something, end is funished")
    while True:
        line = input(">")
        if line == 'end':
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