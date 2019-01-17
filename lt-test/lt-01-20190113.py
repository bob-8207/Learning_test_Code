# -*- coding:utf-8 -*-

"""
简述：这里有四个数字，分别是：1、2、3、4
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
Python解题思路分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
"""

for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x != y) and (y != z) and (x !=z):
                print(x,y,z)