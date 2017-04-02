#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""unicode"""

import unicodedata

s1 = "spicy jalape\u00f1o"
s2 = "spicy jalapen\u0303o"
print(s1, s2)
print(s1 == s2)

t1 = unicodedata.normalize("NFC", s1)
t2 = unicodedata.normalize("NFC", s2)
print(t1, t2)
print(t1 == t2)

print(ascii(t2))