#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import socket

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

UDP_client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = raw_input('> ')
    if not data:
        break
    # 注意，TCP传送用send， UDP用sendto
    UDP_client_sock.sendto(data, ADDR)
    # 注意，TCP接收用recv， UDP用recvfrom
    data, ADDR = UDP_client_sock.recvfrom(BUFSIZ)
    if not data:
        break
    print data

UDP_client_sock.close()

