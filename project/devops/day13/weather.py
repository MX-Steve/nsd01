import json
import urllib
from urllib.request import urlopen
a=urlopen('http://www.weather.com.cn/data/sk/101010100.html')
data=a.read()
print(json.loads(data))
a.close()
# 中国天气网各城市代码weather_cityId
# https://blog.csdn.net/u013193363/article/details/44851897

# 图片位置
# http://m.weather.com.cn/img/c0.gif

# 中国天气网：www.weather.com.cn
# www.weather.com.cn/data/zs/城市编号.html 城市指数
# www.weather.com.cn/data/sk/城市编号.html 城市实况
# www.weather.com.cn/data/cityinfo/城市编号.html 城市信息
