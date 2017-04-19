#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""对数值进行取整"""

print(round(1.23, 1))
print(round(1.27, 1))
print(round(0.22, 1))

a = 133456
print(round(a, -1))
print(round(a, -2))

b = 1.23456
print(format(b, "0.2f"))
print(format(b, "0.4f"))

"""执行精确的小数计算"""

a = 4.2
b = 3.1
c = a + b
print(c)
print(round(c, 2))

from decimal import Decimal
a = Decimal("4.2")
b = Decimal("3.1")
c = a + b
print(c)

from decimal import localcontext
a = Decimal("1.3")
b = Decimal("2.7")
print(a/b)
with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)

"""二进制、八进制和十六进制"""
# bin(), oct(), hex()

x = 12345
# 有前缀
print(bin(x))
print(oct(x))
print(hex(x))

# 无前缀
print(format(x, "b"))
print(format(x, "o"))
print(format(x, "x"))

# 转换至十进制

print(int("11000000111001", 2))
print(int("30071", 8))
print(int("3039", 16))

"""从字节串中打包和解包大整数"""

data = b"\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004"

print(len(data))
print(int.from_bytes(data, "little"))
print(int.from_bytes(data, "big"))

# 重新转换成字节串
x = 94522842520747284487117727783387188
print(x.to_bytes(16, "big"))
print(x.to_bytes(16, "little"))

"""负数运算"""

a = complex(4, 2)
b = 3 - 5j
print(a, b)

# 实部
print(a.real)

# 虚部
print(a.imag)

# 共轭
print(a.conjugate())

# 计算
print(a+b)
print(a-b)
print(a/b)
print(a*b)
print(abs(a))

"""处理无穷大和NaN"""

a = float("inf")
b = float("-inf")
c = float("nan")
print(a, b, c)

import math
print(math.isinf(a))
print(math.isnan(c))

# 计算
print(a+45)
print(a*5)
print(10/a)

# 未定义行为会产生NaN结果
print(a/a)
print(a+b)
# NaN通过任何操作都不会产生异常
print(1/c)

d = float("nan")
# NaN作比较时不会被判定为相等
print(c == d)

"""分数的计算"""

from fractions import Fraction
a = Fraction(10, 3)
b = Fraction(4, 7)
print(a+b, a-b, a/b, a*b)

c = a / b
print(c.numerator, c.denominator)
print(float(c))

# 以5为分母，最接近c的分数
print(c.limit_denominator(5))
print(float(c.limit_denominator(5)))

