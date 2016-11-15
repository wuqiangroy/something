#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 实现数字自动转换英文

li_1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
li_2 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
li_3 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

while True:
    words = raw_input('请输入一个数（1-1000）：')
    if len(words) == 1:
        print li_1[int(words) - 1]
    elif len(words) == 2:
        if int(words) < 20:
            print li_2[int(words) - 11]
        elif int(words[1]) == 0:
            print li_3[int(words[0])-2]
        else:
            print li_3[int(words[0])-2], li_1[int(words[1])-1]
    else:
        if int(words[1]) == int(words[2]) == 0:
            print li_1[int(words[0]) - 1], 'hundred'
        elif int(words[1]) == 0 :
            print li_1[int(words[0]) - 1], 'hundred and', li_1[int(words[2]) - 1]
        else:
            print li_1[int(words[0]) - 1], 'hundred and', li_3[int(words[1])-2], li_1[int(words[2])-1]

