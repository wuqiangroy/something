#!usr/bin/env python
# _*_ coding:utf-8 _*_

from nameko.rpc import rpc


class GreetingService(object):
    name = "greeting"

    @rpc
    def hello(self, name):
        return "Hello, {}".format(name)
