#import urllib.request
#html=urllib.request.urlopen('http://www.baidu.com/')
#print(html.read(20))
#print(html.readline())
#print(html.readlines())
#print(html.read(10))
import sys
from urllib.request import urlopen

def get_web(url,fname):
	html=urlopen(url)
	with open(fname,'wb') as fobj:
		while True:
			data=html.read(4096)
			if not data:
				break
			fobj.write(data)
	html.close()


if __name__=="__main__":
	get_web(sys.argv[1],sys.argv[2])
