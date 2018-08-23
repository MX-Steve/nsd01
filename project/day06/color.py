def colors(func):
    def set_color():
        return '\033[31;1m%s\033[1m' % func()

    return set_color


@colors
def hello():
    return "hello world!"


@colors
def welcome():
    return "welcome china"


if __name__ == '__main__':
    print(hello())
    print(welcome())
    print("========")
    print(colors(hello)())
    print(colors(welcome)())
    print("========")
    print(hello())
    print(welcome()

          )