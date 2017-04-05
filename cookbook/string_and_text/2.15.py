#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys

"""插值"""


class safesub(dict):
    def __missing__(self, key):
        return "{" + key + "}"


def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


name = "wuqiang"
n = 24
print(sub("Hello {name}"))
print(sub("You have {n} messages"))
print(sub("There are {m} trees"))
