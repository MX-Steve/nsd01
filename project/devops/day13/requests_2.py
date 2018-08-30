import requests
#data={'key1':'value1','key2':'value2'}
#r=requests.put('http://httpbin.org/put',data=data)
#r=requests.get('http://httpbin.org/get',params=data)
#print(r.content)# r.content输出搜索到的内容
#######################################################
#payload={"wd":"hello world"}
#r=requests.get('http://www.baidu.com/s',params=payload)
#data=r.content
#with open('/tmp/bbb.html','wb') as fobj:
#	fobj.write(data)
#####################################################
r=requests.get('http://www.baidu.com')
r.encoding='utf8'
print(r.text)
