#!usr/bin/env python
# _*_ coding:utf-8 _*_

from itertools import zip_longest

# 同时迭代多个序列

a = [1, 2, 3, 4, 5, 6]
b = [10, 9, 8, 7, 6, 5]

for x, y in zip(a, b):
    print(x, y)

for i in zip(a, b):
    print(i)

c = [1, 2, 3]
d = ["a", "b", "c", "d"]

for i in zip(c, d):
    print(i)

for i in zip_longest(c, d):
    print(i)        # 多一个（None，d）
for i in zip_longest(c, d, fillvalue=0):
    print(i)