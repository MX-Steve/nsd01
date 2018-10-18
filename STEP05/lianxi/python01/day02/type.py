py_str="python"
print(py_str)
alist=[10,20,30,'abc']
blist = alist
blist.append(100)
print(alist)
clist = alist.copy()
clist.append(200)
print(alist)
print(clist)