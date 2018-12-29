# -*— coding:utf-8 -*-
import datetime

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
        # 营业范围时间
        open_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '8:30', '%Y-%m-%d%H:%M')
        end_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '23:00', '%Y-%m-%d%H:%M')
        # 当前时间
        now_time = datetime.datetime.now()
        if now_time > open_time and now_time < end_time:
            print("现在是 " + str(now_time.strftime('%Y-%m-%d %H:%M')) + ",正在营业中，欢迎光临!")
        else:
            print("现在是 " + str(now_time.strftime('%Y-%m-%d %H:%M')) + ",已经停业，欢迎明天光临!")


    def set_number_served(self, set_served):
        """设置用餐人数"""
        self.number_served = set_served
        print("现在有 " + str(self.number_served) + " 位客人正在就餐！")

    def increment_number_served(self, up_served):
        """
        增用餐人数
        判断用餐人数是否超过接待上限，提升还能接待多少客人
        """
        self.number_served += up_served

        if self.number_served <= 100 :
            print("现在有 " + str(self.number_served) + " 位客人正在就餐！")
        else:
            self.number_served -= up_served
            max_served = 100 - self.number_served
            print("只能再接待" + str(max_served) + "位新来的客人了！" )


#打印餐馆简介和主营菜系
restaurant = Restaurant('蜀味居', '川菜')
print('<<<' + restaurant.restaurant_name + '>>>')
restaurant.describle_restaurant()
print()

#根据系统时间判断是否在营业时间
restaurant.open_restaurant()
print()

#通过调用方法设置或递增用餐人数
restaurant.set_number_served(30)
restaurant.increment_number_served(100)





