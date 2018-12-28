# -*— coding:utf-8 -*-

class Restaurant():
    """这是一个模拟餐馆的小实例"""
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_type
        self.number_served = 0

    def describle_restaurant(self):
        """打印餐馆的简介信息"""
        print(self.restaurant_name + "是一家百年老店，主营正宗" + self.cuisine_name + "，味道正宗！")

    def open_restaurant(self):
        """打印餐馆的营业状态"""
        print("正在营业，欢迎光临！")

restaurant = Restaurant('蜀味居', '川菜')
print('<<<' + restaurant.restaurant_name + '>>>')
restaurant.describle_restaurant()
restaurant.open_restaurant()
print("现在有 " + str(restaurant.number_served) + " 位客人正在就餐！")


