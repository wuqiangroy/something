#!usr/bin/env python
# _*_ coding:utf-8 _*_

import time
import socket
from threading import Thread


# start and stop threading
def countdown(n):
    while n > 0:
        print("T-minus", n)
        n -= 1
        time.sleep(5)

# daemon设置为True表示守护线程
# t = Thread(target=countdown, args=(10,), daemon=True)
# t = Thread(target=countdown, args=(10,))
# t.start()


# 终止线程
class CountDownTask():
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = True

    def run(self, n):
        while self._running and n > 0:
            print("T-minus", n)
            n -= 1
            time.sleep(3)

c = CountDownTask()
t = Thread(target=c.run, args=(10, ))
t.start()
c.terminate()
t.join()


# 设置超时循环
class IOTask():

    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)
        while self._running:
            try:
                data = sock.recv(8192)
                break
            except socket.timeout:
                continue

        return