#!usr/bin/env python
# _*_ coding:utf-8 _*_

# 使用生成器创建新的迭代模式


def frange(start, end, step=1):
    x = start
    while x < end:
        yield x
        x += step

if __name__ == "__main__":
    for n in frange(0, 4, 0.5):
        print(n)
