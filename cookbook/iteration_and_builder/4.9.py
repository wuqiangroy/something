#!usr/bin/env python
# _*_ coding:utf-8 _*_

# 迭代所有可能的组合或排列

from itertools import permutations, combinations
from itertools import combinations_with_replacement


items = [1, 2, 3, 4, 5]
for p in permutations(items):
    print(p)

for p in permutations(items, 2):
    print(p)

for c in combinations(items, 3):
    print(c)

# 相同元素可以多次选择
for c in combinations_with_replacement(items, 3):
    print(c)
