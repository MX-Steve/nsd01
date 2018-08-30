"""
第归：sort中快速排序
"""
from random import randint


def qsort(nums_list):
    if len(nums_list) <2:
        return nums_list
    middle = nums_list[0]
    smaller=[]
    larger=[]
    for i in nums_list[1:]:
        if i < middle:
            smaller.append(i)
        else:
            larger.append(i)

    return qsort(smaller)+[middle]+qsort(larger)


if __name__ == '__main__':
    nums_list = [randint(1, 100) for i in range(1, 10)]
    print(nums_list)
    print(qsort(nums_list))
