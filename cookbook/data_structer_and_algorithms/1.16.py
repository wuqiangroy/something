#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""generator"""


list = [1, 2, 3, 4, -1, 0, -5, 6]

lst1 = [i for i in list if i > 0]
print(type(lst1), lst1)

lst2 = (i for i in list if i > 0)
print(type(lst2), lst2)

address = ["chengdu", "nanjing", "beijing", "shanghai", "guangzhou", "shenzhen"]
count = [1, 4, 6, 2, 6, 8]

more1 = [i > 5 for i in count]
print(more1)

from itertools import compress
more2 = compress(address, more1)
print(more2)
