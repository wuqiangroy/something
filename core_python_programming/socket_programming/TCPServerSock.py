#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import socket
from time import ctime

# TCP服务
TCP_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# UDP服务
UDP_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 创建一个TCP服务器
HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

TCP_sock.bind(ADDR)
TCP_sock.listen(5)

while True:
    print(u'等待联接……')
    TCP_client_sock, addr = TCP_sock.accept()
    print('connecting from:', addr)

    while True:
        data = TCP_client_sock.recv(BUFSIZ)
        if not data:
            break
        TCP_client_sock.send('[%s] %s' % (ctime(), data))
# 程序不能运行到这里，因为上面是死循环
# 提醒，要设计一个更为智能的退出方案，比如服务器要通知关闭的时候，要确保close()函数能调用
TCP_sock.close()



