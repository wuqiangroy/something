#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
选择排序：
1、在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
2、剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3、以此类推，直到所有元素均排序完毕
"""


def selection_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    for i in range(n-1):
        key = i     # 假设我这个数为最小数
        for j in range(i+1, n):
            if lst[key] > lst[j]:
                key = j     # 剩余数中，如果这个数大，那么就和对比的数交换
        if key != i:
            lst[key], lst[i] = lst[i], lst[key]
    return lst

if __name__ == '__main__':
    lst = [5, 9, 6, 3, 4, 1, 0, 3, 2, 8]
    print selection_sort(lst)
