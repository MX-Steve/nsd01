#from urllib.request import urlopen
import json
import requests

def get_weather(city_code):
	url="http://www.weather.com.cn/data/sk/%s.html" % city_code
	#html=urlopen(url)
	#data=html.read()
	#data=json.loads(data)
	r=requests.get(url)
	r.encoding="utf-8"
	data=r.json()
	output="风向： %s ,风力：%s，温度：%s，湿度：%s" % (
		data["weatherinfo"]['WD'],
		data["weatherinfo"]['WS'],
		data["weatherinfo"]['temp'],
		data["weatherinfo"]['SD']
	)
	return output

if __name__=="__main__":

	city_codes={"0":"101010100","1":"101280101","2":"101210101"}
	prompt="""(0) 北京
(1) 广州
(2) 杭州
(3) 成都
请选择(0/1/2/3):
"""
	choice=input(prompt)
	print(get_weather(city_codes[choice]))
