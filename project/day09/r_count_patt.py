import re
"""
re模块提供正则支持，
  compile方法接收一个字符串，并将字符串转换为正则实例
  search方法从内容中找出匹配正则实例的行
  group方法将正则匹配的值去除
"""
def count_patt(fname,patt):
  patt_dict={}
  cpatt = re.compile(patt)
  with open(fname) as fobj:
    for line in fobj:
      m=cpatt.search(line)
      if m:
        key=m.group()
        patt_dict[key]=patt_dict.get(key,0) + 1
  return patt_dict

if __name__=="__main__":
  fname = "access-log"
  ip='^(\d+\.){3}\d+'
  pdict=count_patt(fname,ip)
  print(pdict)
  br = 'Firefox|MSIE|Chrome'
  brs=count_patt(fname,br)
  print(brs)
  shell='bah$|nologin$'
  shells=count_patt('/etc/passwd',shell)
  print(shells)
