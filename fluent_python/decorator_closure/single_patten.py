from functools import wraps


def single(cls):
    pattern = {}
    def decorator(*args, **kwargs):
        if cls not in pattern:
            # print(cls)
            pattern[cls] = cls(*args, **kwargs)
        print(pattern)
        return pattern[cls]
        # return cls(*args, **kwargs)
    return decorator


@single
class test_single:
    a = 4

a1 = test_single()
print(a1.a)
a2 = test_single()
print(a2.a)
print(a1 is a2)