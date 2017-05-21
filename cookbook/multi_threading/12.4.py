#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""對臨界區加鎖"""

import threading


class SharedCounter(object):

    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):

        self._value_lock.acquire()
        self._value += delta
        self._value_lock.release()

        # with self._value_lock:
        #     self._value += delta

    def decr(self, delta=1):
        self._value_lock.acquire()
        self._value -= delta
        self._value_lock.release()

        # with self._value_lock:
        #     self._value -= delta
