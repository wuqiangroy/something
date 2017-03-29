#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import re

line = "something you like, and no one else"

split_line = re.split(r"[;, \s]\s*", line)
split_line2 = re.split(r"(;|,|\s)\s*", line)
print(split_line)
print(split_line2)
