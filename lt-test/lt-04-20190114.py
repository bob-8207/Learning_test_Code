# -*— coding:utf-8 -*-

"""
简述：要求输入某年某月某日 提问：求判断输入日期是当年中的第几天？
Python解题思路分析： 我们就以3月5日这一天为例。首先把前两个月的加起来，
然后再加上5天即本年的第几天。这里有一种特殊的情况，就是闰月，遇到这种情况且输入月份大于2时需考虑多加一天。
如果不是很明白，可以看下边的python源码。
"""
year = int(input("输入年份：\n"))
month = int(input("输入月份：\n"))
day = int(input("输入日期：\n"))
temp = 0

leiji_day = [0,31,59,90,120,151,181,212,243,273,304,334]

temp = leiji_day[month-1] + day

run = 0

if month > 2 and ((year % 400 == 0) or ((year % 4 == 0)and(year % 100 != 0))):
    run = 1
    temp = temp + run
    print(str(year) + '年是闰年\n')
    print(str(year) + '年' + str(month) + '月' + str(day) + '日,是当年的第' + str(temp) + '天')

else:
    print(str(year) + '年' + str(month) + '月' + str(day) + '日,是当年的第' + str(temp) + '天')