#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""whatever capital words"""

import re

text = "UPPER PYTHON, lower python, Mixed Python."

# flags, re.IGNORECSE,忽略大小写
res = re.findall("python", text, flags=re.IGNORECASE)
print(res)

# 替换
res = re.sub("PYTHON", "snake", text, flags=re.IGNORECASE)
# 大小写不匹配
print(res)


def matchcase(word):
    def replace(x):
        text = x.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace
res = re.sub("python", matchcase("snake"), text, flags=re.IGNORECASE)
print(res)
