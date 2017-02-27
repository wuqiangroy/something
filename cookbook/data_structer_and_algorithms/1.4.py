#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
在某个集合中找到最大或最小的N个元素
使用heapq中的nlargest()和nsmallest()
"""

import heapq

nums = [1, 4, 5, 3, 6, 7, 9, 2, 11, 32, 56, 12]

print(heapq.nlargest(4, nums))
# [56, 32, 12, 11]
print(heapq.nsmallest(4, nums))
# [1, 2, 3, 4]

"""
接受参数
"""

people = [
    {'name': 'xiaoming', 'age': 14, 'sexual': 'male'},
    {'name': 'xiaohong', 'age': 13, 'sexual': 'female'},
    {'name': 'taotao', 'age': 15, 'sexual': 'male'},
    {'name': 'zhangbo', 'age': 21, 'sexual': 'male'},
    {'name': 'jingjing', 'age': 11, 'sexual': 'female'},
    {'name': 'sichuan', 'age': 16, 'sexual': 'male'},
]

print(heapq.nlargest(2, people, key=lambda x: x['age']))
print(heapq.nsmallest(2, people, key=lambda x: x['age']))
