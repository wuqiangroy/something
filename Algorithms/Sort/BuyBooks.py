#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 买书，输入n个人的书，和n个书的ISBN值。
# 输出，n本书，去重的ISBN值，按照从小到达排列。

# 法一， 先去重，再排序。利用桶排序


def buy_books(lst):
    res = [0] * max(max(lst)+1, len(lst))
    for i in lst:
        res[i] = 1
    return res


lst = [12, 13, 14, 12, 14]


lst = buy_books(lst)
for i in range(len(lst)):
    if lst[i] != 0:
        print i,


# 法二，先排序，再去重，利用冒泡排序


def buy_books2(lst):
    n = len(lst)
    while n:
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
        n -= 1
    for i in range(len(lst)):
        if lst[i] == lst[i-1]:
            continue
        print lst[i],

lst2 = [22, 13, 12, 43, 33, 7, 2, 12, 22]
buy_books2(lst2)

