#!usr/bin/env python
# _*_ coding:utf-8 _*_

# 反向迭代

# reversed()
a = [1, 2, 3, 4, 5]
for x in reversed(a):
    print(x)


# 自定义__reversed__()
class CountDown(object):

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

if __name__ == "__main__":
    c = CountDown(5)
    for i in c:
        print(i)
        