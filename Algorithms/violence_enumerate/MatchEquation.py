#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
n根火柴棍，摆出A + B = C的等式
1、加号与等号分别需要两根
2、A ≠ B，则 A + B 和 B + A 视为不同等式
3、所有火柴棍必须用到
4、m ≤ 24
"""

import time

match_dict = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}


def match_nums(x):
    x = str(x)
    nums = 0
    for i in x:
        nums += match_dict[i]
    return nums


def main(n):
    for a in xrange(1000):
        for b in xrange(1000):
            c = a + b
            if match_nums(a) + match_nums(b) + match_nums(c) == n - 4:
                print('{0} + {1} = {2}'.format(a, b, c))


if __name__ == '__main__':
    n = 18
    main(n)



