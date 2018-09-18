import time


# 法1
# def timeit(func):
#     start = time.time()
#     func()
#     end = time.time()
#     print(end - start)

def deco(func):
    def timeit():
        start = time.time()
        func()
        end = time.time()
        print(end - start)

    return timeit


@deco
def funca():
    time.sleep(5)


@deco
def funcb():
    print("hello world")


if __name__ == '__main__':
# 法1
# timeit(funca)
# timeit(funcb)
    funca()
    funcb()
