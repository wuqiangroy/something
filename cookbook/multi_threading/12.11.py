#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""实现发布者/订阅者消息模式"""

from collections import defaultdict


class Exchange(object):
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

_exchange = defaultdict(Exchange)


def get_exchange(name):
    return _exchange[name]
