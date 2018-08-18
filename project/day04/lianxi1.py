#/usr/local/bin/python3

"""
创建文件练习:
1.think about the process of the apps
2.create a function including all actions
3.write the function
"""

import os

def get_fname():
    while True:
        fname = input("请输入文件名:")
        if not os.path.exists(fname):
            break
        print("%s already exits, try again"%(fname))
    return fname

def get_content():
    content = []
    print("请输入正文,end结束:")
    while True:
        line = input(">")
        if line == "end":
            break
        content.append(line)
    return content

def write_file(fname,content):
    fname_obj = open(fname,'w')
    fname_obj.writelines(content)


if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ["%s\n" % line for line in content]
    write_file(fname,content)

