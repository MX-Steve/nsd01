#!/usr/bin/env python3
"""
判断变量起名是否合法
1.变量名不能是关键字
2.变量名不能以数字开头
3.变量名不能包含特殊字符
"""
from keyword import iskeyword
from string import ascii_letters, digits

first_letter = ascii_letters + "_"
other_letters = first_letter + digits


def check_id(name):
    # 判断是否是关键字
    if iskeyword(name):
        return "%s 是关键字" % name
    # 判断手字符
    if name[0] not in first_letter:
        return "首字符包含了特殊字符"
    # 判断其他字符
    for ind, ch in enumerate(name[1:]):
        if ch not in other_letters:
            return "第%s 不合法" % (ind + 2)
    return "%s 可以使用" % name


if __name__ == '__main__':
    name = input("请输入你要检查的变量名:")
    print(check_id(name))
