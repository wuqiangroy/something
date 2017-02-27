#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
保存最后N个元素
对一系列文本进行匹配，发现有匹配时就输出当前匹配行以及最后检查过的N行文本
"""

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    f = '''
    I am a handsome boy,
    I try my best to open a new world!
    '''
    for line, prevlines in search(f, 'o', 5):
        for pline in prevlines:
            print(pline)
        print(line)
        print('-'*20)
