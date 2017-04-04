#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""format text"""

text = "Hello World!"

print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print("=="*20)

print(text.ljust(20, "="))
print(text.rjust(20, "-"))
print(text.center(20, "*"))
print("=="*20)
# >右对齐， <左对齐，^居中
print(format(text, ">20"))
print(format(text, "<20"))
print(format(text, "^20"))
print("=="*20)

print(format(text, "=>20"))
print(format(text, "-<20"))
print(format(text, "*^20"))
print("=="*20)

print("{:>10s} {:>10s}".format("Hello", "world"))

x = 1.2345
print(format(x, "^10.2f"))
