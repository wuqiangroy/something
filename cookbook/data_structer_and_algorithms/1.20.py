#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""多个映射合并为单个映射"""

from collections import ChainMap

a = {"x": 2, "z": 3}
b = {"y": 4, "z": 6}

# c = ChainMap(a, b)
c = ChainMap(b, a)

print(c["x"])
print(c["y"])
# c值取决于谁在chainmap前面
print(c["z"])

c["x"] = 3
print(c["x"])

