#!usr/bin/env python
# _*_ coding:utf-8 _*_

"""在类和静态方法上使用装饰器"""

import time
from functools import wraps


def time_it(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, "use {} ms".format((end-start)*1000))
        return res
    return wrapper


class Spam(object):

    @time_it
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @time_it
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @time_it
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1

s = Spam()
s.instance_method(1000000)
Spam.class_method(1000000)
Spam.static_method(1000000)
