# -*— coding:utf-8 -*-

"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契以兔子繁殖为例子而引入，故又称为“兔子数列”，
指的是这样一个数列：1、1、2、3、5、8、13、21、34、....
在数学上，斐波纳契数列以如下被以递归的方法定义:

F0 = 0               (n=0)
F1 = 1               (n=1)
Fn = F[n-1]+F[n-2]   (n=>2)

要求一：输出第10个斐波那契数列
要求二：问题的要求改为：需要输出指定个数的斐波那契数列
"""

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a

def fib2(n2):
    if n2 ==1 or n2 ==2:
        return 1
    return fib2(n2-1)+fib2(n2-2)


def fib3(m):
    x,y = 1,1
    l = [1,1]
    for j in range(m-2):
        x,y = y,x+y

        l.append(y)
    return l


t = fib(10)
print(t)

t2 = fib2(10)
print(t2)

t3 = fib3(10)
print(t3)