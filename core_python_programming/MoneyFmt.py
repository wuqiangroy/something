#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
浮点值作为输入，返回一个字符串形式金额数：
比如
>>>12346678.9
$12,346,678.9
负数要显示在$前面
"""


class MoneyFmt(object):
    def __init__(self, value=0.0):
        self.value = float(value)

    def dollarize(self):
        pos_num = abs(self.value)
        list_pos_num = str(pos_num).split('.')
        str_money = list_pos_num[0]
        last_money = list(list_pos_num[1])
        if len(str_money) <= 3:
            if self.value < 0:
                doc_money = ''.join(['-']+['$'] + list(str(pos_num)))
            else:
                doc_money = ''.join(['$'] + list(str(pos_num)))
        else:
            new_lis = list(str_money)
            if len(str_money) % 3 == 0:
                num = len(str_money) / 3 - 1
            else:
                num = len(str_money) / 3
            for n in range(0, num):
                new_lis.insert((-3+(-4*n)), ',')
            if self.value < 0:
                doc_money = ''.join(['-'] + ['$'] + new_lis + ['.'] + last_money)
            else:
                doc_money = ''.join(['$'] + new_lis + ['.'] + last_money)
        return doc_money

m = MoneyFmt(123456.89)
print m.dollarize()


