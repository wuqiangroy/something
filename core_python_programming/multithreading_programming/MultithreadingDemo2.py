#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import threading
import time

loops = [4, 2]


class ThreadingFunc(object):

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.res = self.func(*self.args)


def loop(nloop, nsec):
    print('starting loop', nloop, 'at:', time.ctime())
    time.sleep(nsec)
    print('loop', nloop, 'done at:', time.ctime())


def main():
    print('starting at:', time.ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        # 在ThreadingFunc类中，把loop函数、(i, loops[i])带入，name即loop的名字。
        t = threading.Thread(
            target=ThreadingFunc(loop, (i, loops[i]),
                                 loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('all DONE at:', time.ctime())


if __name__ == '__main__':
    main()
