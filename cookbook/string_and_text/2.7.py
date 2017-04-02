#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""shortest match"""

import re

text1 = "I want to say:'Hello, World!'"
text2 = "I love this 'lovely' world, and 'ugly' people."

patch = re.compile(r"\'(.*)\'")
print(patch.findall(text1))
# 中间的字符被匹配出来 ["lovely' world, and 'ugly"]
print(patch.findall(text2))

patch2 = re.compile(r"\'(.*?)\'")
print(patch2.findall(text1))
# 最短匹配 ['lovely', 'ugly']
print(patch2.findall(text2))
