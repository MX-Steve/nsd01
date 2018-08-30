# 生成器：
def mygen():
    yield "hello world"
    a = 10 + 20
    yield a
    yield [10, 20]


def block(fobj):
    content = []
    counter = 0
    for line in fobj:
        content.append(line)
        counter += 1
        if counter == 10:
            yield content
            content = []
            counter = 0
    if content:
        yield content


if __name__ == '__main__':
    # a = mygen()
    # #一个生成器只能用一回
    # for item in a:
    #     print(item)
    # b=mygen()
    # for item in b:
    #     print(item)

    with open('/tmp/passwd') as fobj:
        for lines in block(fobj):
            print(lines)
            print()
