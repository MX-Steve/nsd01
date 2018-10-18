def fun1():
    print("hello world!")

#fun1()

def fun2():
    fib = [0,1]
    l = int(input("length:"))
    for i in range(l-2):
        fib.append(fib[-1]+fib[-2])
    print(fib)

#fun2()

def fun3(n=10):
    fib = [0,1]
    l = int(n)
    for i in range(l-2):
        fib.append(fib[-1]+fib[-2])
    return fib

# n = input("length")
# print(fun3(n))

print(fun3(20))
print(fun3())