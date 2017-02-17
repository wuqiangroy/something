#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 冒泡排序，相邻元素相互比较。
# 缺点：时间复杂度特别高(n^2) 优点：容易理解、代码简洁、不耗费额外空间


def bubble_sort(lst):
    n = len(lst)
    while n:
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n -= 1
    return lst

if __name__ == '__main__':
    lst = [1, 3, 5, 6, 3, 1, 9, 2, 1, 8, 5]
    print bubble_sort(lst)
