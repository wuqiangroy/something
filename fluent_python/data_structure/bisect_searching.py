# _*_ uft-8 _*_

import sys
import bisect
import random


haystack = [1, 3, 4, 6, 7, 8, 9, 11, 15, 19, 22, 29, 33, 41, 54]
needles = [0, 1, 2, 4, 10, 23, 30, 31]

row_fmt = "{0:2d} @ {1:2d}    {2}{0:<2d}"


def demo(bisect_fun):
    for needle in reversed(needles):
        position = bisect_fun(haystack, needle)
        offset = position * "  |"
        print(row_fmt.format(needle, position, offset))


def insert(size):
    random.seed(1729)
    my_list = []
    for i in range(size):
        new_item = random.randrange(size*2)
        bisect.insort(my_list, new_item)
        print("%2d ->" % new_item, my_list)

if __name__ == "__main__":
    if sys.argv[-1] == "left":
        bisect_fun = bisect.bisect_left
    else:
        bisect_fun = bisect.bisect

    print("Demo: ", bisect_fun.__name__)
    print("haystack -> ", " ".join("%2d" % n for n in haystack))
    print(demo(bisect_fun))
    insert(7)
