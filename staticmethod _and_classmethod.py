#!usr/bin/env python
# _*_ coding:utf-8 _*_

"""what's difference between classmethod and staticmethod"""


class Kls(object):
    no_ins = 0

    def __init__(self):
        Kls.no_ins += 1

    @classmethod
    def get_no_of_ins(cls):
        print(cls.no_ins)

kls1 = Kls()
kls2 = Kls()
kls3 = Kls()
kls1.get_no_of_ins()

IND = "ON"


class Cls(object):

    def __init__(self, data):
        self.data = data

    @staticmethod
    def checkind():
        return (IND == "ON")

    def de_reset(self):
        if self.checkind():
            print("Reset dong for: {}".format(self.data))

    def set_db(self):
        if self.checkind():
            self.db = "New db connection"
        print("DB connection made for: {}".format(self.data))

cls1 = Cls(12)
cls1.de_reset()
cls1.set_db()


class Ikl(object):

    def __init__(self, data):
        self.data = data

    def printd(self):
        print(self.data)

    @staticmethod
    def smethod(*args):
        print("Staticmethod: {}".format(args))

    @classmethod
    def cmethod(cls, *args):
        print("Classmethod: {}".format(args))

ik = Ikl(23)
ik.printd()
ik.smethod()
ik.cmethod()
Ikl.smethod()
Ikl.cmethod()
