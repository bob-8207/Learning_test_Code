# -*— coding:utf-8 -*-

class User():

    def __init__(self, first_name, last_name, age, national):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.national = national

    def describle_user(self):
        print('#' * 50 )
        print('First name: ' + self.first_name)
        print('Last name: ' + self.last_name)
        print('Age: ' + str(self.age))
        print('National: ' + self.national)
        print('#' * 50)

    def greet_user(self):
        print('hi！' + self.last_name + ':')
        print("北京欢迎你，希望在北京过的愉快！")

Liu_weinong = User('Liu', 'Weinong', 58, 'USA')
Liu_weinong.describle_user()
Liu_weinong.greet_user()

print()

Yang_bo = User('Yang', 'Bo', 36, 'China')
Yang_bo.describle_user()
Yang_bo.greet_user()
