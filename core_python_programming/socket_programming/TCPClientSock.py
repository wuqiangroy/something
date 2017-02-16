#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import socket

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

TCP_client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TCP_client_sock.connect(ADDR)

while True:
    data = raw_input('> ')
    if not data:
        break
    TCP_client_sock.send(data)
    data = TCP_client_sock.recv(BUFSIZ)
    if not data:
        break
    print(data)

TCP_client_sock.close()
