#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import urlparse
import json
from cgi import escape
from urlparse import parse_qs


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    params = parse_qs(environ['QUERY_STRING'])
    name = params.get('name', [''])[0]
    website = params.get('website', [''])[0]
    user = params.get('user', [''])[0]
    password = params.get('pass', [''])[0]
    dic = [{'name': name, 'website': website, 'user': user,
            'password': password}]
    data = {'data': dic}
    return json.dumps(data)