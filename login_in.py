#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 设计一个登录系统
import sys

name_pwd = {}

def new_user():
    while True:
        name = raw_input("昵称：\n")
        if name_pwd.has_key(name):
            print "昵称已经被人占了，请换一个吧。"
            continue
        else:
            while True:
                pwd = raw_input("请输入密码：\n")
                pwd2 = raw_input("请确认密码：\n")
                if pwd == pwd2:
                    name_pwd[name] = pwd
                    break
                else:
                    print "两次密码不相同，请重新输入！"
                    continue
        break

def old_user():
    while True:
        name = raw_input('请输入用户名：\n')
        if name_pwd.has_key(name):
            pwd = raw_input("请输入密码：\n")
            if name_pwd[name] == pwd:
                print name, "欢迎回来！"
                break
            else:
                print "密码错误！"
                continue
        else:
            print "没有这个用户名，请重新输入！"
            continue

def menu():
    menu =  '''
    (N)新用户
    (O)老用户
    (Q)退出

    请选择！
    '''
    flag = False
    while not flag:
        chose = False
        while not chose:
            try:
                choice = raw_input(menu).strip()[0]
                if choice == 'N':
                    new_user()
                elif choice == 'O':
                    old_user()
            except(EOFError, KeyboardInterrupt):
                choice = 'Q'
                print "你选择了退出系统！"
                sys.exit()
            if choice not in 'NOQ':
                print "请重新输入！"
            else:
                chose = True
                flag = True

if __name__ == '__main__':
    menu()




