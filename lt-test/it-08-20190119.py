# -*- coding:utf-8 -*-

"""
简述：9*9乘法口诀表。
要求：逐项单位输出。例如1的一行，2的一行，以此类推。
Python解题思路分析：
注意分行与列考虑。这里共有9行和9列。x控制行，y控制列。

"""
for x in range(1,10):
    for y in range(1,1+x):
        print('{0}*{1}='.format(x,y),x*y,end=' ')
    print()