#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 生产者消费者模型
# 生产货物时间不确定，消费者消耗货物时间也不确定
# 生产和消费不对应，由于线程原因，所以我们要加线程锁

import time
from random import randint
from Queue import Queue
import threading


class Producer(threading.Thread):
    def __init__(self, name, queue):
        self.__name = name
        self.__queue = queue
        super(Producer, self).__init__()

    def run(self):
        while True:
            if self.__queue.full():
                time.sleep(randint(2, 5))
            else:
                self.__queue.put('cake')
                time.sleep(randint(2, 5))
                print('Now are %s cakes, %s creates a cake.' %
                      (self.__queue.qsize(), self.__name))


class Consumer(threading.Thread):
    def __init__(self, name, queue):
        self.__name = name
        self.__queue = queue
        super(Consumer, self).__init__()

    def run(self):
        while True:
            if self.__queue.empty():
                time.sleep(randint(5, 10))
            else:
                self.__queue.get('cake')
                time.sleep(randint(2, 5))
                print('Now are %s cake, consumer%s boughts a cake.' %
                      (self.__queue.qsize(), self.__name))

queue = Queue(maxsize=100)
creates = ['John', 'Marry', 'Peter']
consumers = range(randint(15, 20))
lock = threading.Lock()

# 将线程加锁。
for i in creates:
    lock.acquire()
    # 生产
    Producer(i, queue).start()
    lock.release()

for i in consumers:
    lock.acquire()
    # 消费
    Consumer(i, queue).start()
    lock.release()
