astr='\thello  '
print(astr)
#去空格:
astr.strip() #去空白字符两端
astr.lstrip() #去左
astr.rstrip() #去右

#
hi = "hello world"
hi.title() # 单词首字母大写
hi.upper() # 大写
hi.lower() # 小写
hi.islower() # 判断是否小写,可以有数字
hi.isdigit() # 是否是数字
hi.isidentifier() # 布判断关键字,判断是合法变量不
hi.center(50)
hi.center(50,"#")
hi.ljust(50)
hi.rjust(50)
hi.startswith('fa')
hi.endswith('d')
hi.split('.') # 以.切割
