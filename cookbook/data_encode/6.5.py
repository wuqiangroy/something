#!usr/bin/env python
# _*_ coding:utf-8 _*_

# 将字典转换为xml

from xml.etree.ElementTree import Element, tostring


def dic_to_xml(tag, d):

    ele = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        ele.append(child)
    return ele

d = {"name": "GOGO", "shares": 100, "price": 490.1}
e = dic_to_xml("stock", d)
print(e)
print(tostring(e))
e.set("_id", "12344321")
print(tostring(e))
