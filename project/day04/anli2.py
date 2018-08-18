#!/usr/bin/env python3
"""
检查标示符
1.先获得用户的标示符
2.判断标示符
"""
# print(keyword.kwlist)
from string import ascii_letters, digits
from keyword import iskeyword

first_chs = ascii_letters + "_"
other_chs = first_chs + digits


def check_id(idt):
    if iskeyword(idt):
        return "%s is keyword" % idt  # 函数只会执行一个return
    if idt[0] not in first_chs:
        return "lst invalid!"
    for ind, ch in enumerate(idt[1:]):
        if ch not in other_chs:
            return "第%s 个字符不合法" % (ind + 2)
    return "%s 是合法的!" % idt


if __name__ == '__main__':
    idt = input("待检查的标示符:")
    print(check_id(idt))
