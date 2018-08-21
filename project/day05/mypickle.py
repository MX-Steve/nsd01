# import pickle as p
# #可以将任意的数据类型写入文件,可以无损取出
# shopping = '/tmp/shop.txt'
# shop_list=['apple','eggs','banana']
# with open(shopping,'wb') as fobj:
#     p.dump(shop_list,fobj)  #将列表写入文件
# with open(shopping,'rb') as fobj:
#     mylist = p.load(fobj) #从文件中取出的数据仍然是列表
# print(mylist[1])

# import pickle as p
# shop_file="/tmp/shop.txt"
# shop_list=['egg','apple','banana']
# with open(shop_file,'wb') as fobj:
#     p.dump(shop_list,fobj)
# with open(shop_file,'rb') as fobj:
#     mylist=p.load(fobj)
# print(mylist[1])

# import pickle as p
# shop_file="/tmp/shop.txt"
# shop_list=['apple','books','ages']
# with open(shop_file,'wb') as fobj:
#     p.dump(shop_list,fobj)
# with open(shop_file,'rb') as fobj:
#     mylist=p.load(fobj)
# print(mylist)

import pickle as p
shop_list=['a','b','c','d']
shop_file="/tmp/shop.txt"
with open(shop_file,'wb') as fobj:
    p.dump(shop_list,fobj)
with open(shop_file,'rb') as fobj:
    mylist=p.load(fobj)
print(mylist)