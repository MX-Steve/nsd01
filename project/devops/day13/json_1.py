import json

#number=json.dumps(100)
#print(json.loads(number))

#print(json.dumps([1,2,3]))
import urllib
from urllib.request import urlopen
a=urlopen('http://www.weather.com.cn/data/sk/101010100.html')
data=a.read()
print(json.loads(data))
