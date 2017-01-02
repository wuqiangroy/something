#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从小到大自动排列

"""

a = raw_input('第一个数： ')
b = raw_input('第二个数： ')
c = raw_input('第三个数： ')

if a < b:
    if a < c < b:
        print a, c, b
    elif a < c and b < c:
        print a, b, c
    else:
        print c, a, b
else:
    if b < c < a:
        print b, c, a
    elif b < c and a < c:
        print b, a, c
    else:
        print c, b, a
