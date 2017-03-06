#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import urlparse
import json
from cgi import escape
from urlparse import parse_qs


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = "http://%s?%s" % (environ['HTTP_HOST'], environ['QUERY_STRING'])
    if len(environ['QUERY_STRING']) > 0:
        query = urlparse.urlparse(url).query
        dic = dict([(k, v[0]) for k, v in urlparse.parse_qs(query).items])
        data = {'data': dic}
        return json.dumps(data)
    else:
        return json.dumps({'data': url})

