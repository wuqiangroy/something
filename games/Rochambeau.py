#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 石头剪刀布游戏
'''
Created on 2016/11/14

Created by WuQiang
'''

from random import choice

li = ['石头', '剪刀', '布']
rules = [['石头', '剪刀'], ['剪刀', '布'], ['布', '石头'], ]
while True:
    n = input('请输入你出的： \n')
    N = choice(li)
    if n == N:
        print("你出 %s， 电脑出 %s， 平局!" % (n, N))
    elif [n, N] in rules:
        print("你出 %s， 电脑出 %s， 恭喜你获胜!" % (n, N))
    else:
        print("你出 %s， 电脑出 %s， 很遗憾，你输了!" % (n, N))
