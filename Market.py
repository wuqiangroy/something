#_*_coding:utf-8_*_

import sys

salary = int(raw_input("Please enter your current salary: "))
shopping_car = {}  # 将购物车设置为一个字典

vanue = {
        'Car':500000, 'Macbook':20000, 
        'Computer':5000, 'Bike':2000,
        'MI':1999, 'Book':500, 
        'Earpod':299, 'Cup': 100,
        'Coffee': 30, 'Joice':5
        }  # 将购物车中产品和价格做成字典。产品对应价格
while True:
    print "You have %s money now, all the things are here!" % salary
    print """
                shopping list
    --------------------------------------
    Car                             500000
    Macbook                          20000
    Computer                          5000
    Bike                              2000
    MI                                1999
    Book                               500
    Earpod                             299
    Cup                                100
    Coffee                              30
    Joice                                5
    --------------------------------------
    """
    name = raw_input("Which one do you want to buy? enter exit to exit.\n")
    if name in vanue:  # 检测输入的产品是否在字典vanue里面
        price = vanue[name]  # 利用字典将产品名和价格对应，这一步price = 产品价格
        if price <= salary:
            salary -= price  # 剩余的钱为薪水减去价格
            if name in shopping_car:  # 判断购买的商品是否在购物车里面
                shopping_car[name][1] += 1  # 如果在，那么购物车中数量+1
            else:
                shopping_car[name] = [price, 1]  # 不在，就添加一个新的物品信息进去
        else:
            print "You can't afford %s, please choose again!" % name
            continue
    elif "exit" in name:
        print '''
                shopping car
            -------------------
            name  price  number
            '''
        for i in shopping_car:
            print i, shopping_car[i][0], shopping_car[i][1]
        
        print "You just have %s money." % salary
        sys.exit()
    else: 
        print "You only can buy the thing in shopping list! please choose again!"
        continue
    
