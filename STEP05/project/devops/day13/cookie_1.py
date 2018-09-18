import requests
r=requests.get('http://www.dangdang.com')
co=r.cookies
r1=requests.get('http://www.dangdang.com',cookies=co)
