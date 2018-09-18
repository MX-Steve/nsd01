#!/usr/bin/env python3
"""
字符串的使用基础
"""
sentence = 'tom\'s pet is a cat'
sentence1 = "tom's pet is a cat"
sentence2 = "tom said:\"hello world!\""
sentence3 = 'tom said:"hello world!"'
words = """
hello
world
abcd"""
py_str='python'
len(py_str)
py_str[0]
'python'[0]
py_str[-1]
py_str[2:4]
py_str[2:]
py_str[:2]
py1 = py_str[:]
print(id(py_str),id(py1))
print(py_str + "is good")
print(py_str*3)
print('t' in py_str)
print('th' in py_str)
print('to' not in py_str)





