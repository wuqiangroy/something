#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import socket

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

while True:
    TCP_client_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCP_client_server.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    TCP_client_server.send('%s \r\n' % data)
    data = TCP_client_server.recv(BUFSIZ)
    if not data:
        break
    print(data.strip())
    TCP_client_server.close()
