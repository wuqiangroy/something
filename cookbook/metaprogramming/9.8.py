#!usr/bin/env python
# _*_ coding:utf-8 _*_

"""类中定义装饰器"""

from functools import wraps


class A:

    # decorator as a instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 1")
            return func(*args, **kwargs)
        return wrapper

    # decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 2")
            return func(*args, **kwargs)
        return wrapper

a = A()


# as a instance method
@a.decorator1
def spam():
    print("Spam")


# as a class method
@A.decorator2
def add(x, y):
    print(x**y)

spam()
add(2, 3)
