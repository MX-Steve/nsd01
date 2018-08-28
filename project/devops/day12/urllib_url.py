import re
import sys

def get_url(patt,fname):
	cpatt=re.compile(patt)
	result=[]
	with open(fname) as fobj:
		for line in fobj:
			m=cpatt.search(line)
			if m:
				result.append(m.group())
		return result
	
	

if __name__ =="__main__":
	url=r'http://[\w/.-]+\.(jpg|jpeg|png|gif)'
	print(get_url(url,sys.argv[1]))
