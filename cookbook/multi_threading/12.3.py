#!usr/bin/env python
# _*_ coding:utf-8 _*_

# 线程间通信， queue， Queue,
# 生产者、消费者模型

import time
from queue import Queue
from threading import Thread, Lock


# def product(out_q):
#     while True:
#         out_q.put(data)
#
#
# def consumer(in_q):
#     while True:
#         data = in_q.get()
#
# q = Queue()
# t1 = Thread(target=consumer, args=(q,))
# t2 = Thread(target=product, args=(q,))
# t1.start()
# t2.start()

# _sentinel = object()
#
#
# def product(out_q):
#     while running:
#         out_q.put(data)
#
#     out_q.put(_sentinel)
#
#
# def consumer(in_q):
#     while True:
#         data = in_q.get()
#
#         if data is _sentinel:
#             in_q.put(_sentinel)
#             break


def producer(in_q):
    while True:
        if in_q.full():
            time.sleep(5)
        else:
            in_q.put("hamburger")
            time.sleep(2)
            print("product 1 hamburger, remaining {} hamburger".format(in_q.qsize()))


def consumer(out_q):
    while True:
        if out_q.empty():
            time.sleep(2)
        else:
            out_q.get("hamburger")
            time.sleep(2)
            print("use 1 hamburger, remaining {} hamburger".format(out_q.qsize()))

queue = Queue(maxsize=50)
t1 = Thread(target=producer, args=(queue,))
t2 = Thread(target=consumer, args=(queue,))
t1.start()
t2.start()
