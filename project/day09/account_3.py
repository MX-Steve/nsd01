import re
from collections import Counter


class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        cpatt = re.compile(patt)
        patt_obj = Counter()
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    item = m.group()
                    patt_obj.update([item])
        return patt_obj


if __name__ == '__main__':
    fname = "access-log"
    ip = "^(\d+\.){3}\d+"
    web_log = CountPatt(fname)
    a = web_log.count_patt(ip)
    print(a)
    print(a.most_common(3))
