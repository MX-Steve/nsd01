import json
import urllib
from urllib.request import urlopen
a=urlopen('http://www.weather.com.cn/data/sk/101010100.html')
data=a.read()
print(json.loads(data))
a.close()

# 图片位置
# http://m.weather.com.cn/img/c0.gif
