#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""named tuple"""

from collections import namedtuple

sub = namedtuple("Sub", ["add", "phone"])
res = sub("chengdu", "18208106521")

print(res)
print(res.add)
print(res.phone)

res = sub(add="Pidu", phone="18180410723")
print(res.add, res.phone)
