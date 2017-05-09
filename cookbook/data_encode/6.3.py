#!usr/bin/env python
# _*_ coding:utf-8 _*_

# 处理xml


from urllib.request import urlopen
from xml.etree.ElementTree import parse

u = urlopen("http://planet.python.org/rss20.xml")
doc = parse(u)

for i in doc.iterfind("channel/item"):
    title = i.findtext("title")
    date = i.findtext("pubDate")
    link = i.findtext("link")

    print(title)
    print(date)
    print(link)