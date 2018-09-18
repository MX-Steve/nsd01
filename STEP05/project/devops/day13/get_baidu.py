import requests
r=requests.get('http://www.baidu.com')
r.encoding='utf-8'
with open("/tmp/badu.html",'w') as fobj:
	fobj.write(r.text)
# r.text 查看纯文本
# r.content 可以看纯文本或者图片,对非文本有帮助,返回字节形式
# r.json() 看json，返回json格式，适用于各种对象
print(r.status_code)
