#!/user/bin/env python
# _*_coding:utf-8_*_
import itertools
number = raw_input("请随意输入一个整数：")
li = []
li_2 = []
for i in number:
    li.append(i)
li_3 = list(itertools.permutations(li, len(li)))
for n in li_3:
    li_2.append(int("".join(list(n))))
max_number = max(li_2)
print '-1' if max_number == int(number) else max_number

def next_big(n):
    list_data=[int(i) for i in str(n)] #将n转换str，然后遍历，将遍历元素int后加入list_data列表
    tmp=list_data ==reversed(list_data) #将list_data列表倒置
    res=[]
    while len(list_data)>0:
        res.append(max(list_data)) # 循环将list_data中最大的元素加入res列表
        del list_data[list_data.index(max(list_data))] # 删除list_data中最大的元素
    return -1 if tmp else int("".join([str(i) for i in res]))  #在res中的元素遍历后定义为str然后转换为list，再int。
print next_big(555)




