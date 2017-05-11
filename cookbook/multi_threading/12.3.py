#!usr/bin/env python
# _*_ coding:utf-8 _*_

# 线程间通信， queue， Queue,
# 生产者、消费者模型

from queue import Queue
from threading import Thread


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

