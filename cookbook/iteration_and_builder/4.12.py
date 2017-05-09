#!usr/bin/env python
# _*_ coding:utf-8 _*_

# 在不同的容器中进行迭代

from itertools import chain

a = [1, 2, 3, 4, 5]
b = [11, 12, 13, 14, 15]
# 依次迭代
for x in chain(a, b):
    print(x)
