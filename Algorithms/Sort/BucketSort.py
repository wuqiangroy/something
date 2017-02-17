#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 桶排序
# 缺点：浪费空间，只能是正整数


def bucket_sort(lst):
    res = [0] * max(len(lst), max(lst)+1)
    for i in lst:
        res[i] += 1
    return res

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 2, 9, 4, 6, 8, 0, 1, 1, 3, 2, 2, 2, 2]
    lst = bucket_sort(lst)

    for i in range(len(lst)):
        if lst[i] != 0:
            j = lst[i]
            while j:
                print i,
                j -= 1
