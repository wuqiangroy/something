#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 使用栈来判断回文， 回文特点：先入后出
"""
方法：
1、找到需要判断的字符串的中间点
2、将前部分加入栈
3、取出栈里的数据，然后对比剩下的数据，相同就是回文
"""


def determin_palindrome(st):
    n = len(st)
    # 找到中间点
    mid = n / 2
    # 将st在mid前面的数据加入栈
    stack = [i for i in st[:mid]]
    # 取出在栈中的数据
    new_st = []
    while stack:
        # 将stack中的数据取出加入新列表
        new_st.append(stack.pop())
    if st[mid:] == ''.join(new_st) or st[mid+1:] == ''.join(new_st):
        return True
    return False

if __name__ == '__main__':
    st = 'wuquw'
    st2 = 'wuuw'
    st3 = 'wuqiang'
    print determin_palindrome(st)
    print determin_palindrome(st2)
    print determin_palindrome(st3)


