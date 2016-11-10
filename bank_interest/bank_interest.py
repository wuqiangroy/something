#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 计算银行利息

def invest(amount, rate, year):
    for t in range(1, year + 1):
        amount = amount * (1 + rate)
        print "第{0}年，本息共{1}元。" .format(t, amount)

amount = float(raw_input('请输入存的金额：  '))
rate = float(raw_input('请输入年利率：  '))
year = int(raw_input('请输入要存的年数：'))

invest(amount, rate, year)