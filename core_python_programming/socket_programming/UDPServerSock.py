#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import socket
from time import ctime

# 注意，TCP是SOCK.STREAM流套接字， UDP是SOCK.DGRAM数据报
UDP_server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

UDP_server_sock.bind(ADDR)

while True:
    print(u'等待消息……')
    data, addr = UDP_server_sock.recvfrom(BUFSIZ)
    UDP_server_sock.sendto('[%s], %s' % (ctime(), data), addr)
    print('...receive from and returned to:', addr)

UDP_server_sock.close()



