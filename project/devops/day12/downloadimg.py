from urllib_url import get_url
from urllib_2 import get_data
import os

url=r'http://[\w/.-]+\.(jpg|jpeg|png|gif)'
get_data('http://www.tmooc.cn/','/tmp/bbb.html')
urls=get_url(url,'/tmp/bbb.html')

img_dir='/tmp/images'
if not os.path.exists(img_dir):
	os.mkdir(img_dir)

for url in urls:
	fname=url.split('/')[-1]
	fname=os.path.join(img_dir,fname)
	get_data(url,fname)
