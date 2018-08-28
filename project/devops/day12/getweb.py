from urllib.request import urlopen
import sys
from urllib.request import Request

def get_web(url,fname):
	header = {
		"User-Agent":"Mozilla/5.0 (X11;Fedora;Linux x86_64) AppleWebkit/537.36 (KHTML,like Gecko) Chrome/58.0.3029.110 Safari/537.36"
	}
	request=Request(url,headers=header)
	html=urlopen(request)
	with open(fname,'wb') as fobj:
		while True:
			line=html.read(4096)
			if not line:
				break
			fobj.write(line)
	html.close()	

if __name__=="__main__":
	get_web(sys.argv[1],sys.argv[2])
