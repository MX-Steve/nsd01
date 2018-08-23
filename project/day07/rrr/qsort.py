"""
排序：数据结构和算法
1.快速排序
"""
from random import randint


def qsort(nums_list):
    if len(nums_list) < 2:
        return nums_list
    else:
        middle = nums_list[0]
        smaller = []
        larger = []
        for i in nums_list[1:]:
            if i <= middle:
                smaller.append(i)
            else:
                larger.append(i)
        return qsort(smaller) + [middle] + qsort(larger)
        # qsort(smaller)
        # qsort(larger)


if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    print(qsort(nums))
