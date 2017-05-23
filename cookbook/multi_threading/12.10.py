#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
定义一个actor任务
actor是最古老最简单的解决并发和分布式计算问题的方法之一
"""

from queue import Queue
from threading import Thread, Event


class ActorExit(Exception):
    pass


class Actor(object):
    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._terminated = Event()
        t = Thread(target=self._bootstrap)
        t.daemon = True
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        while True:
            msg = self.recv()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print("Got:", msg)

p = PrintActor()
p.start()
p.send("Hello")
p.send("World")
p.close()
p.join()

