#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
插入排序：
1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5
"""


def insertion_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    for i in range(1, n):
        for j in range(i, 0, -1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]

    return lst


def insertion_sort2(lst):
    n = len(lst)
    if n == 1:
        return lst
    for i in range(1, n):
        key = lst[i]    # 已排序的元素
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

if __name__ == '__main__':
    lst = [2, 3, 5, 2, 7, 5, 4, 3]
    print insertion_sort(lst)
    print insertion_sort2(lst)
