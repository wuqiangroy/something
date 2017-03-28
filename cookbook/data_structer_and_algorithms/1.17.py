#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""创建一个字典，本身是另一个字典的子集"""

# 字典推导式(dictionary comprehension), 速度很快，快于大部分其余方法
dic = {
    "ACME": 45.32,
    "AAPL": 612.78,
    "HPQ": 37.20,
    "IBM": 205.55,
    "FB": 10.75,
}

# 速度快
p1 = {key: value for key, value in dic.items() if value > 200}
# 速度慢
p1_1 = dict((key, value) for key, value in dic.items() if value > 200)

tech_name = {"AAPL", "IBM", "HPQ", "MSFT"}
p2 = {key: value for key, value in dic.items() if key in tech_name}

print(type(tech_name))
print(p1)
print(p2)
