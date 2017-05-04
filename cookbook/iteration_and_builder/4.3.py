#!usr/bin/env python
# _*_ coding:utf-8 _*_

# 使用生成器创建新的迭代模式


def frange(start, end, step=1):
    x = start
    while x < end:
        yield x
        x += step


# yield底层机智
def countdown(n):
    print("Starting count from", n)
    while n > 0:
        yield n
        n -= 1
    print("Finish")

if __name__ == "__main__":
    # for n in frange(0, 4, 0.5):
    #     print(n)
    c = countdown(3)
    print(next(c))
    print(next(c))
    print(next(c))
