import time


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
    # start1 = time.time()
    # funca()
    # end1 = time.time()
    # print(end1 - start1)
    # start2 = time.time()
    # funcb()
    # end2 = time.time()
    # print(end2 - start2)
    funca()
    funcb()
