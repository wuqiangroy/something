#!usr/bin/env python
# _*_ coding:utf-8 _*_

"""属性可修改装饰器"""

import logging
from functools import wraps, partial


def attach_wrapper(obj, func=None):

    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):

    def decorate(func):
        logname = name if name else func.__name__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(new_level):
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)
        def set_msg(new_msg):
            nonlocal logmsg
            logmsg = new_msg

        return wrapper
    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, "example")
def spam():
    print("Spam")

logging.basicConfig(level=logging.DEBUG)
print(add(5, 10))

add.set_msg("Add called")
print(add(2, 3))

add.set_level(logging.WARNING)
print(add(5, 6))
