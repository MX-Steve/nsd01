import time
#人头
i=0
print("\033[33;1m#\033[0m"*45)
while i < 20:
    j=0
    while j < 45:
        if j == 0 or j == 44:
            print("\033[33;1m#\033[0m",end="")
        #眼睛
        elif (3 <=j<=11) and (2<=i<=3) :
            print("\033[31;1m#\033[0m",end="")
        elif (11 <j<32) and i==2 :
            print(" ", end="")
        elif 4<=i<=10 and (5<=j<=7 or 35<=j<=37):
            print("#",end="")
        # 嘴巴
        elif (32 <=j<=40) and (2<=i<=3) :
            print("\033[31;1m#\033[0m", end="")
        elif (15<=j<=30) and (i==12 or i==14):
            print("\033[32;1m#\033[0m", end="")
        elif (15<=j<=17 or 20<j<=25 or 28<=j<=30) and (i==13):
            print("\033[30;1m#\033[0m", end="")
        #鼻子
        elif (7<=i<=10) and (21<=j<=23):
            print("\033[33;1m#\033[0m", end="")
        else:
            print(" ",end="")

        j+=1
    i+=1
    print()
print("\033[33;1m#\033[0m"*45)
