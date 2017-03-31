#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re
from calendar import month_abbr

"""replace"""

text = "today is 31/3/2017, and yesterday is 30/3/2017."

re_text = text.replace("today", "this day")
print(re_text)

re_text2 = re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\2-\1", text)
print(re_text2)

# 可以循环使用
patch = re.compile(r"(\d+)/(\d+)/(\d+)")

re_text3 = patch.sub(r"\3-\2-\1", text)
print(re_text3)


def change_date(x):
    mon_name = month_abbr[int(x.group(2))]
    return "{} {} {}".format(x.group(1), mon_name, x.group(3))

# 可以设置回调函数
print(patch.sub(change_date, text))


