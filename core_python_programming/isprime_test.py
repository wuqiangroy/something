#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
判断输入的一个数是否为素数
"""


def isprime(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
        else:
            continue
    if len(lst) == 2:
        return True
    else:
        return False
if __name__ == '__main__':
    n = input('请输入一个数 :  ')
    print (isprime(n))