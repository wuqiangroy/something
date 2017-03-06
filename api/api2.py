#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import urlparse
import json
from cgi import escape
from urlparse import parse_qs


def application(environ, start_response):
    start_response('200, OK', [('Content-Type', 'text/html')])
    headers = '%s' % (environ)
    url = 'http://%s?%s' % (environ['HTTP_PORT'], environ['QUERY_STRING'])
    query = urlparse.urlparse(url).query
    gets = dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items()])
    code = 200
    username = environ['HTTP_USER_NAME']
    password = environ['HTTP_PASS_WORD']
    coding = environ['HTTP_CODING']
    sub_headers = {'username': username, 'password': password,
                   'coding': coding}
    data = {'headers': sub_headers, 'gets': gets, 'code': code}
    return json.dumps(data)