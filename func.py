#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@gmail.com
@software: garner
@file: func.py.py
@time: 2018/5/12/012 17:47
@desc:
'''
# 本节学习创建python函数，并调用
# def myfuntion():
#     print("my name is ren yingming,i'm 24 years old")
#     return
# 开始调用,输入函数名，然后点击运行即可
# myfuntion()
# *arg是可变参数，以元组形式返回
# **kwargs是关键字参数，返回结果以字典形式
# def myfun(name,old,*args,**kwargs):
#     print('my name is %s,i\'m %d years old'%(name,old))
#     print(args)
#     print(kwargs)
#     # return
# myfun('li li',100,1,2,3,me='ren',ear=2)
# 2带return的返回
# def myfun(name,old,*args,**kwargs):
#     print('my name is %s,i\'m %d years old'%(name,old))
#     print(args)
#     print(kwargs)
#     return 'yeah,this is first my function'
# result=myfun('li li',100,1,2,3,me='ren',ear=2)
# print('result:',result)

# 1\自定义一个计算奇数的函数
# def countfunc(start,end):
#     sum=0
#     for i in range(start,end):
#         if i%2 !=0:
#             sum += i
#     return sum
# count=countfunc(1,100)
# print(count)
# 2,while循环控制条件
# def count_func(start,end):
#     sum=0
#     while start <= end:
#         if start % 2!=0:
#             sum += start
#         start +=1
#     return sum
# count=count_func(1,100)
# print(count)

# 匿名函数lambda
# print(type(lambda :print('a')))
# a=lambda :print('ming')
# a()
'''
写一个函数，该函数能判断传入的参数是否是一个完数，如果是完数则返回True，否则返回False
提示：完数就是一个数等于他的因子之和，如6=1+2+3; 那么这个数就是完数。
'''
#copy
#  l = [ ]
# for n in range (1,10000):
#     for a in range (1,n):
#         if n%a ==0:
#             l.append(a)
#     if sum(l)==n:
#         print (l)
#         print (n)
#     l = []

# def perfect(n):
#     total=0
#     for i in range(1,n):
#         if n % i == 0:
#             total += i
#     if total == n:
#         return True
#     else:
#         return False
# a = perfect(6)
# print(a)

# format的格式化的使用
# print('{},{},{}'.format('name',12,'man'))
# print('{0},{1}'.format('zhangk', 32))
#
# print('{},{},{}'.format('zhangk', 'boy', 32))
#
# print('{name},{sex},{age}'.format(age=32, sex='male', name='zhangk'))
#
# # 格式限定符
# # 它有着丰富的的“格式限定符”（语法是{}中带:号），比如：
#
# # 填充与对齐
# # 填充常跟对齐一起使用
# # ^、<、>分别是居中、左对齐、右对齐，后面带宽度
# # :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
#
# print('{:>8}'.format('zhang'))
# print('{:0>8}'.format('zhang'))
# print('{:a<8}'.format('zhang'))
# print('{:p^10}'.format('zhang'))
#
# # 精度与类型f
# # 精度常跟类型f一起使用
# print('{:.2f}'.format(31.31412))
#
# # 其他类型
# # 主要就是进制了，b、d、o、x分别是二进制、十进制、八进制、十六进制
# print('{:b}'.format(15))
#
# print('{:d}'.format(15))
#
# print('{:o}'.format(15))
#
# print('{:x}'.format(15))
#
# # 用逗号还能用来做金额的千位分隔符
# print('{:,}'.format(123456789))

# 自定义函数求完数
def perfect_number(n):
    sum=0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    if n == sum:
        return True
    else:
        return False
a=perfect_number(28)
print(a)
# 求10000以内的完数
# for n in range(1,10001):
#     if perfect_number(n):
#         print('this is perfect number in range(1,10001):{}'.format(n))
