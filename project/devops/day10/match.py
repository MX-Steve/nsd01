#http://down.51cto.com  ==><正则表达式必知必会>
import re


# 正则表达式贪婪匹配
data = 'my phone number : 1501234565'
m = re.search('.+(\d+)', data)
print(m.group())
print(m.group(1))
#默认+*都是贪婪匹配，在其后面加上？就让?右边的模式尽量多的匹配
n=re.search('.+?(\d+)',data)
print(n.group(1))
