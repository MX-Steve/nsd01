# 将爬取到的源码中的图片取出并下载
from urllib_url import get_url
# 用来爬取网站源码
from urllib_2 import get_data
import os

# 获取源码文件
get_data('http://www.tmooc.cn/','/tmp/bbb.html')
# 编写图片正则
url=r'http://[\w/.-]+\.(jpg|jpeg|png|gif)'
# 从图片正则下载并存储图片
urls=get_url(url,'/tmp/bbb.html')

img_dir='/tmp/images'
if not os.path.exists(img_dir):
	os.mkdir(img_dir)

for url in urls:
	fname=os.path.join(img_dir,url.split('/')[-1])
	try:
		get_data(url,fname)
	except:
		pass
