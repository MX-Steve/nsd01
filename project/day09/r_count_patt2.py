import re
from collections import Counter
"""
collections 模块提供数据集合排序汇总
  Counter算法：字典的子类，排序字典,跟踪值出现的次数
	update:将传过来的值传递给Counter，并进行计数
	most_common(3)从多到少进行排序，3为只排序前三
re模块提供正则支持，
  compile方法接收一个字符串，并将字符串转换为正则实例
  search方法从内容中找出匹配正则实例的行
  group方法将正则匹配的值去除
"""


class CounterPatt:
  def __init__(self,fname):
    self.fname=fname

  def count_patt(self,patt):
    cpatt = re.compile(patt)
    patt_obj = Counter()
    with open(self.fname) as fobj:
      for line in fobj:
        m = cpatt.search(line)
        if m:
          item = m.group()
          patt_obj.update([item])
    return patt_obj

if __name__=="__main__":
  fname = "access-log"
  ip = '^(\d+\.){3}\d+'
  web_log=CounterPatt(fname)
  a = web_log.count_patt(ip)
  print(a)
  print(a.most_common(3))
  b = web_log.count_patt('Firefox|MSIE|Chrome')
  print(b)
  print(b.most_common(5)) 


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
"""
