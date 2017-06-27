#!usr/bin/env python
# _*_ coding:utf-8 _*_

"""把装饰器定义成类"""

import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


# use in func
@Profiled
def add(x, y):
    print(x+y)


# use in class
class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)

add(4, 5)
Spam().bar(6)
