#!usr/bin/env python
# _*_ coding:utf-8 _*_

"""用装饰器执行类型检查"""


from functools import wraps
from inspect import signature


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)

            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            "Argument {} must be {}".format(
                                name, bound_types[name])
                        )
            return func(*args, **kwargs)
        return wrapper
    return decorate


@typeassert(int, z=int)
def spam(x, y, z):
    return x, y, z

print(spam(23, 14, "hello, world"))
