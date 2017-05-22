#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""保存线程专有状态"""

import threading
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection(object):

    def __init__(self, address, family=AF_INET, stream=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = stream
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, "sock"):
            raise RuntimeError("Already connected")
        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock


def connect(conn):
    with conn as c:
        c.send(b"GET /index.html HTTP/1.0 \r\n")
        c.send(b"HOST: www.python.org\r\n")
        c.send(b"\r\n")
        res = b"".join(iter(partial(c.recv, 8192), b""))

    print("Got {} bytes".format(len(res)))

if __name__ == "__main__":
    conn = LazyConnection(("www.python.org", 80))

    t1 = threading.Thread(target=connect, args=(conn, ))
    t2 = threading.Thread(target=connect, args=(conn, ))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
