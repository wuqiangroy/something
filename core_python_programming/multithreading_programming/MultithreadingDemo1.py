#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import time
import threading

loops = [4, 2]


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', time.ctime())
    time.sleep(nsec)
    print('loop', nloop, 'done at:', time.ctime())


def main():
    print('starting at:', time.ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,
                             args=(i, loops[i]))
        threads.append(t)

    # start thread
    for i in nloops:
        threads[i].start()

    # wait for all
    for i in nloops:
        # threads to finish
        # 阻塞线程直到线程结束。如果没有join，那么就会执行all Done at
        threads[i].join()

    print('all DONE at:', time.ctime())


if __name__ == '__main__':
    main()
