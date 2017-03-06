#!/usr/bin/env python
# _*_ coding:utf-8 _*_

from wsgiref.simple_server import make_server
from api2 import application

httpd = make_server('172.0.0.1', 8000, application)
print('Serving HTTP on port 8000……')
httpd.serve_forever()
