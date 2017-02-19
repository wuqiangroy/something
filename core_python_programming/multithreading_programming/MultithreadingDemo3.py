#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import threading
import time

loops = [4, 2]


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        # 调用父类多线程的构造函数
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        apply(self.func, self.args)


def loop(nloop, nsec):
        print('start loop', nloop, 'at:', time.ctime())
        time.sleep(nsec)
        print('loop', nloop, 'done at:', time.ctime())


def main():
    print('starting at:', time.ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        # 类MyThread中已经调用了多线程的构造函数，所以这里不需要再次调用。
        # 这里相当于:threading.Thread(target=func(*args))
        t = MyThread(loop, (i, loops[i]),
                     loop.__name__)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print('All DONE at:', time.ctime())


if __name__ == '__main__':
    main()
