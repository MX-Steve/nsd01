import re
from collections import Counter

class CountPatt:
    def __init__(self,fname):
        self.fname=fname

if __name__ == '__main__':
    fname='access-log'
    ip='^(\d+\.){3}\d+'
    web_log=CountPatt(fname)
    a=web_log.count_patt(ip)
    print(a)
    print(a.most_common(3))