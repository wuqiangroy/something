#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""创建线程池"""

from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor


def echo_client(socket, client_addr):

    print("Got connection from", client_addr)
    while True:
        msg = socket.recv(65536)
        if not msg:
            break
        socket.sendall(msg)
    print("Client closed connection")
    socket.close()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)

echo_server(("", 15000))
