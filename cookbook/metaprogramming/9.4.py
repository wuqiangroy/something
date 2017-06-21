#!usr/bin/env python
# _*_ coding:utf-8 _*_

"""传参装饰器"""

from functools import wraps
import logging


def logged(level, name=None, message=None):

    def decorator(func):
        logname = name if name else func.__name__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level=level, msg=logmsg)
            return func(*args, **kwargs)
        return wrapper
    return decorator


@logged(logging.DEBUG)
def add(x, y):

    return x + y


@logged(logging.CRITICAL)
def spam():
    print("Spam")

print(add(5, 10))
spam()
