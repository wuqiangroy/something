#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""re"""

import re

date = "31/3/2017"
date2 = "today is 31/3/2017, it's remind me of 31/3/1997"
# \d表示一个数字，后面+表示多个数字
# 另一种写法findall(r"\d+/\d+/\d+", date)
patch = re.compile(r"\d+/\d+/\d+")

if patch.match(date):
    print(True)
else:
    print(False)

# 多重查找
print(patch.findall(date2))

# 加括号简化后续操作
patch2 = re.compile(r"(\d+)/(\d+)/(\d+)")
m = patch2.match(date)
# m为一个对象
print(m)
print(m.groups())
print(m.group(1))
print(m.group(2))
print(m.group(3))
print("-"*10)
for day, month, year in patch2.findall(date2):
    print("{}-{}-{}".format(year, month, day))
