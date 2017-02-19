#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 调用myThread模块

from myThread import MyThread
import time


# 斐波拉契数列
def fib(x):
    time.sleep(0.005)
    if x < 2:
        return 1
    return fib(x-1) + fib(x-2)


# 阶乘
def fac(x):
    time.sleep(0.1)
    if x < 2:
        return 1
    return x * fac(x-1)


# 累加
def new_sum(x):
    time.sleep(0.1)
    if x < 2:
        return 1
    return x + new_sum(x-1)

funcs = [fib, fac, new_sum]
n = 12


def main():
    nfunc = range(len(funcs))

    print('*** SINGLE THREAD')
    for i in nfunc:
        print('starting', funcs[i].__name__, 'at:', time.ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', time.ctime())

    print('\n*** MULTITHREADING')
    threads = []
    for i in nfunc:
        t = MyThread(funcs[i], n, funcs[i].__name__)
        threads.append(t)

    for i in nfunc:
        threads[i].start()

    for i in nfunc:
        threads[i].join()
        print(threads[i].get_result())

    print('all DONE')


if __name__ == '__main__':
    main()
