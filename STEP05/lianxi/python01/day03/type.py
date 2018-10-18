astr="python"
alist=[111,22,'abd']
atup = (11,22,33,44)
adict = {"name":"bob","age":23}
for ch in astr:
    print(ch,end=" ")

for name in alist:
    print(name)

for i in atup:
    print(i)

for key in adict:
    print("%s:%s" % (key,adict[key]))