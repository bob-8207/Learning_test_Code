# -*— coding:utf-8 -*-

"""
整数顺序排列问题简述：任意三个整数类型，x、y、z 提问：要求把这三个数，按照由小到大的顺序输出
Python解题思路分析：首先，要想方法把最小的数放到x位上，之后将x与y进行比较； 
如果x>y的话，就将x与y的值进行交换； 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
"""

l = []

for i in range(3):
    x = int(input("输入一个数字："))
    l.append(x)

l.sort()

print('从小到大顺序为：',l)
