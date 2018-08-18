list('abcd')
list((10, 20, 30))
str(10)
str((10, 20, 30))
max([10, 20, 30])
min([10, 20, 30])
max("hello")

users = ['liisi', 'jack', 'tom']
for i in range(len(users)):
    print("#%s:%s" % (i, users[i]))

for i, j in enumerate(users):
    print("#%s:%s" % (i, j))

stus = [
    {"id": 1, "name": "tom"},
    {"id": 2, "name": "lisi"}
]

for index, obj in enumerate(stus):
    print("#%s:%s" % (index, obj['name']))

sorted(users)

for u in reversed(users):
    print(u)

# 字符编码:ASCII
ord('a')
ord('A')
bin(97)
ord("我")
#25105
bin(25105)
#'0b110001000010001'