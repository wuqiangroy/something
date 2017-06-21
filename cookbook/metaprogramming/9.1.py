#!usr/bin/env python
# _*_ coding:utf-8 _*_

"""给函数添加包装 -- 装饰器"""

import time
from functools import wraps


def time_this(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@time_this
def countdown(n):

    while n > 0:
        n -= 1

countdown(100000)
print(countdown.__name__)
countdown(10000000)
