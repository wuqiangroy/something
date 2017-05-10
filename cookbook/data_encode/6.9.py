#!usr/bin/env python
# _*_ coding:utf-8 _*_

# 编码和解码十六进制数字, 转化为字节流

import base64
import binascii

s = b"hello"

# 转化为字节流
h = binascii.b2a_hex(s)
j = base64.b16encode(s)
print(h, j)

# 字节流转化为十六进制

b = binascii.a2b_hex(h)
c = base64.b16decode(j)
print(b, c)




