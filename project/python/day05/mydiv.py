try:
    num=int(input("number"))
    result = 100/num
except (ValueError,ZeroDivisionError):
    print("输入错误") #报相同的错误,可以将错误写在元组里
except KeyboardInterrupt:
    print("\nbye-bye")
except EOFError:
    print("\nbye-bye")
else:
    print(result) #不发生异常才执行的代码
finally:
    print("down") #不管发不发生错误,都执行
