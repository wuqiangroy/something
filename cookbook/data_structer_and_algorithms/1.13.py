#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""sort dict"""


def sort_dict():
    from operator import itemgetter

    rows = [
        {"name": "wuqiang", "age": 23},
        {"name": "zhangpeng", "age": 22},
        {"name": "gaojiuli", "age": 24},
        {"name": "zhangzhe", "age": 96}
    ]
    row_by_name = sorted(rows, key=itemgetter("name"))
    row_by_age = sorted(rows, key=itemgetter("age"))

    print(row_by_name)
    print(row_by_age)

sort_dict()