# -*— coding:utf-8 -*-

class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_name = cuisine_type

    def describle_restaurant(self):
        print(self.restaurant_name + "是一家百年老店，主营正宗" + self.cuisine_name + "，味道正宗！")

    def open_restaurant(self):
        print("正在营业，欢迎光临！")

Chuan_Cai = Restaurant('蜀味居', '川菜')
print('<<<' + Chuan_Cai.restaurant_name + '>>>')
Chuan_Cai.describle_restaurant()
Chuan_Cai.open_restaurant()

Yue_Cai = Restaurant('静风阁', '粤菜')
print('<<<' + Yue_Cai.restaurant_name + '>>>')
Yue_Cai.describle_restaurant()
Yue_Cai.open_restaurant()