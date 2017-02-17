#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from SocketServer import TCPServer as TCP
from SocketServer import StreamRequestHandler as SRH
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)


class MyRequestHandler(SRH):
    def handle(self):
        print('...connecting from', self.client_address)
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

TCPServ = TCP(ADDR, MyRequestHandler)
print('waiting for connecting......')
TCPServ.serve_forever()
