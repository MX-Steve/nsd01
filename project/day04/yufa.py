x = y = 10
print(id(x),id(y))
y = 0
print(id(x),id(y))
a = b = [10,20]
print(id(a),id(b))

a,b = 10,20
a,b = b,a
print(a,b)