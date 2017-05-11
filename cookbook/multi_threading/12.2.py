#!usr/bin/env python
# _*_ coding:utf-8 _*_

# 判断线程是否已经启动

import time
import threading
from threading import Thread, Event


# 单词事件
def countdown(n, start_envent):

    print("countdown starting")
    start_envent.set()
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(3)

start_envent = Event()

# print("Launching countdown")
# t = Thread(target=countdown, args=(10, start_envent))
# t.start()
#
# start_envent.wait()
# print("countdown is running")


# 多次事件
class PeriodicTimer:

    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        # 设置线程保护
        t.daemon = True
        t.start()

    def run(self):
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

primer = PeriodicTimer(5)
primer.start()


def countdown2(nticks):
    while nticks > 0:
        primer.wait_for_tick()
        print("T-minus", nticks)
        nticks -= 1


def countup(last):
    n = 0
    while n < last:
        primer.wait_for_tick()
        print("Counting", n)
        n += 1

threading.Thread(target=countdown2, args=(10,)).start()
threading.Thread(target=countup, args=(5,)).start()
