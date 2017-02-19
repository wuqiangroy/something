#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 多线程运行的模块，可以直接调用运行。

import threading
import time


class MyThread(threading.Thread):

    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
        print('starting', self.name, 'at:', time.ctime())
        self.res = self.func(self.args)
        print(self.name, 'finished at:', time.ctime())

    def get_result(self):
        return self.res


