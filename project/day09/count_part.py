import re

from collections import Counter
c = Counter()
c.update('hello world')



def count_part(fname, patt):
    patt_dict = {}
    cpatt = re.compile(patt)
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                patt_dict[key] = patt_dict.get(key, 0) + 1
                # if key not in patt_dict:
                #     patt_dict[key]=1
                # else:
                #     patt_dict[key]+=1
                # awk '{print $1}' access-log | sort | uniq -c | sort -nr
    return patt_dict


if __name__ == '__main__':
    fname = 'access-log'
    ip = '^(\d+\.){3}\d+'  # 1.2.12.3
    br = 'firefox|MSIE|Chrome'
    print(count_part(fname, br))
    shell = 'bash$|nologin$'
    print(count_part('/etc/passwd', shell))
    fobj=count_part(fname, ip)
    flist = list(fobj.items())
    print(flist)
