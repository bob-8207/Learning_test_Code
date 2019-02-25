# -*- coding:utf-8 -*-

a1 = 1
b2 = 1
for i in range(1,21):
    print('%9ld %9ld'%(a1,b2),end='')
    if i % 3 == 0 :
        print(' ')
    a1 = a1 + b2
    b2 = a1 + b2
