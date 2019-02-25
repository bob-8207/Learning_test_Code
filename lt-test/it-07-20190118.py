# -*- coding:utf-8 -*-

"""
提问：将一个列表的数据复制到另一个列表中。
请仔细看要求，这里要求的是复制数据到一个新的列表中。
Python列表数据复制，Python解题思路分析：可以了解下[  ：]的含义

"""

x = []

for i in range(10):
    x.append(i)
print("x:",x)

y = x[:]

print("y:",y)