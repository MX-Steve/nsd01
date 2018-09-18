from urllib.request import urlopen
import sys

def get_data(url,fname):
	html=urlopen(url)
	with open(fname,'wb') as fobj:
		while True:
			line=html.read(4096)
			if not line:
				break
			fobj.write(line)
	html.close()	

if __name__=="__main__":
	get_data(sys.argv[1],sys.argv[2])
