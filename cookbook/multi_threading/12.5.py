#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""避免死锁"""

import threading
from contextlib import contextmanager

_local = threading.Lock()


@contextmanager
def acquire(*locks):

    locks = sorted(locks, key=lambda x: id(x))

    acquired = getattr(_local, "acquired", [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError("Lock Order Violation")

    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.require()
        yield
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks)]

x_lock = threading.Lock()
y_lock = threading.Lock()


def thread_1():
    while True:
        with acquire(x_lock, y_lock):
            print("Thread-1")


def thread_2():
    while True:
        with acquire(y_lock, x_lock):
            print("Thread-1")

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

t2 = threading.Thread(target=thread_2)
t2.daemon = True
t2.start()
