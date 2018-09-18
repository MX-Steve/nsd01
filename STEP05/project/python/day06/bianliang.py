x = 20


def bar():
    global x
    x = 200


print(x)
bar()
print(x)