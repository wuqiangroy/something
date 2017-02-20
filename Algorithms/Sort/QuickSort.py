#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 快速排序
# 每次排序都设置一个基准点，然后排列，基准点归位后，基准点左右分开排序，再选择基准点排列
# 一般基准点都是左边第一个
# 排序时，从右边出发，遇到第一个比基准点小的停止，从左边出发，遇到比基准点大的停止，两者交换。
# 继续除法，知道左右相遇，这时候把相遇点和基准点交换，排序结束。


def quick_sort(lst, low, high):
    if low < high:
        pivot_index = partion(lst, low, high)
        # 将列表按基准点分开排序
        quick_sort(lst, low, pivot_index)
        quick_sort(lst, pivot_index+1, high)


def partion(lst, low, high):
    key = lst[low]      # 基准点
    while low < high:
        # 右边一直往左走（high -= 1）， 直到小于基准点
        while low < high and lst[high] >= key:
            high -= 1
        # 左右交换
        if low < high:
            lst[low] = lst[high]
        # 左边一直往右走，知道大于基准点
        while low < high and lst[low] < key:
            low += 1
        # 左右交换
        if low < high:
            lst[high] = lst[low]
    # 返回此刻基准点所在的位置
    lst[low] = key
    return low

if __name__ == '__main__':
    lst = [1, 5, 3, 2, 8, 9, 3, 1, 5, 6, 3, 2, 0]
    print(lst)
    quick_sort(lst, 0, len(lst)-1)
    print(lst)


