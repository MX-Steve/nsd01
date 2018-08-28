import sys
from urllib.request import urlopen
import.re

# url:图片网址;dir:图片存放位置
def get_imgs(url,dir):
	html = urlopen(url)
	#编写正则表达式并将匹配的图片结果存在一个列表中
	imgs_reg=()
	#for循环，将列表中的图片结果一个个存入相应的文件



if __name__=="__main__":
	get_imgs(sys.argv[1],sys.argv[2])
