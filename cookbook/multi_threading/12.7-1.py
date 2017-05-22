#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""手动实现线程池"""
from queue import Queue
from threading import Thread
from socket import AF_INET, SOCK_STREAM, socket


def echo_client(q):

    sock, client_addr = q.get()
    print("Got connection from", client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print("Client closed connection")
    sock.close()


def echo_server(addr, workers):

    q = Queue()
    for n in range(workers):
        t = Thread(target=echo_client, args=(q, ))
        t.daemon = True
        t.start()

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        q.put((client_sock, client_addr))

echo_server(("", 15000), 128)
