import requests
pl={'wd':"hello world"}
headers={'Accept':"application/json"}
r=requests.get('http://www.baidu.com/s',params=pl,headers=headers)
r=requests.post('http://www.baidu.com/s',data=pl)
