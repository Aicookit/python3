#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@gmail.com
@software: garner
@file: play1.py
@time: 2018/5/11/011 11:07
@desc:
'''
# import time
#
# now_time=time.localtime()
# print(now_time)
# year=now_time.tm_year
# month=now_time.tm_mon
# mday=now_time.tm_mday
# wday=now_time.tm_wday
# # 判断现在的时间是上旬还是下旬，和是星期几
# result='现在是%s年%s月，还是当月的'%(year,month)
# if mday <= 15:
#     result += '上旬'
# else:
#     result += '下旬'
#
# if wday == 0:
#     result += '，星期一'
# elif wday == 1:
#     result += '，星期二'
# elif wday == 2:
#     result += '，星期三'
# elif wday == 3:
#     result += '，星期四'
# elif wday == 4:
#     result += '，星期五'
# elif wday == 5:
#     result += '，星期六'
# elif wday == 6:
#     result += '，星期日'
# print(result)
# import random
# temp=random.randint(1,16)
# print(temp)

#字典功能
# dictionary={}
# # print(help(dictionary))
# a='wo'
# # b='ai'
# # c='ni'
# # print('%s %s %s'%(a, b ,c))
# while True:
#     a='love'
#     b='dislike'
#     c=input('请输入love or dislike: ')
#
#     if c == a:
#         print('小三')
#         break
#     elif c == b:
#         print('正房')
#         break
#     else:
#         print('难道是小久？请重新输入！')
#         continue
# total=0
# # while 1:
# #     i=0
# #     i += 1                  #冗长版
# #     hah=input('输入：')
# #     total+=i
# #     print(total)

# i=0                             #精简版
# while 1:
#     i+=1
#     hah=input('输入：')
#     print(i)
#     continue

# def kancai(name,age,gender):
#     print('%s,%d岁，%s,上山去砍柴'%(name,age,gender))
#
# a=kancai('xiaoming',18,'nan')

# class Foo:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#     def cutfirewood(self):
#         print('%s,%d岁，%s,上山去砍柴。'%(self.name,self.age,self.gender))
#     def gonortheast(self):
#         print('%s,%d岁,%s,开车去东北。'%(self.name,self.age,self.gender))
#     def fitness(self):
#         print('%s,%d岁，%s,最爱大保健。'%(self.name,self.age,self.gender))
#
# a=Foo('小名',10,'男')          #这里括号里的叫做封装，是面向对象三大特性（封装，继承，多态,但python不支持多态，只崇尚鸭子类型）之一
# a.gonortheast()
# a.fitness()
# a.cutfirewood()
'''
# 程序二：游戏人生程序
# 创建三个人物，分别是：
# 关羽：男，45，初始战斗力：1000
# 貂蝉：女，38，初始战斗力：999
# 刘备：男，45，初始战斗力888
# 游戏场景：
# 草丛战斗：消耗200战力
# 自我修炼：增长100战力
# 多人游戏：消耗500战力
# '''
# class Person:
#     def __init__(self,name,gender,age,figt):
#         self.name=name
#         self.gender=gender
#         self.age=age
#         self.figt=figt
#     def grassland(self):
#         self.figt=self.figt-200
#     def practice(self):
#         self.figt=self.figt+200
#     def incest(self):
#         self.figt=self.figt-500
#     def detail(self):
#         temp='姓名：%s;性别：%s;年龄：%s;战斗力：%s'%(self.name,self.gender,self.age,self.figt)
#         print(temp)
#
# guanyu=Person('关羽','男',48,1000)
# diaocan=Person('貂蝉','女',38,999)
# liubei=Person('刘备','男',45,888)
# guanyu.incest()
# liubei.figt()
# diaocan.incest()

# #继承
# '''
# class Cat:                      #冗余
#     def sound(self):
#         print('喵喵')
#     def eat(self):
#         print('mouse')
#     def move(self):
#         #do something
#
# class Dog:
#     def sound(self):
#         print('汪汪')
#     def eat(self):
#         print('bone')
#     def move(self):
#         #do something
# '''
# #精简
# class Animal:
#     def sound(self):
#         #do something
#     def eat(self):
#         #do something
#     def move(self):
#         #do something
# class Cat(Animal):
#     def sound(self):
#         print('喵喵')
# class Dog(Animal):
#         print('汪汪')

# role={
#     1:{'name':'zhang','gender':'男'},
#     2:{'name':'li','gender':'女'}
# }
# # print(role[2])
# # print(role[1]['name'])
# # print(role[1]['gender'])
# def print_value(d):
#     for key,value in d.items():
#         if isinstance(value,dict):
#             yield from print_value(value)
#         else:
#             yield value
# if __name__=='__main__':
#     for i in print_value(role):
#         print(i)

# a='abck'
# print('我想要%s（字母）'%a[0])

class Dog(object):
    def __init__(self,name,dog_type):
        self.name=name
        self.dog_type=dog_type
    def sayhi(self,weapon='枪'):
        print('%s说：汪汪,我的是属于%s狗,我配有%s'%(self.name,self.dog_type,weapon))
d=Dog('小白','哈巴')
d.sayhi()
a=Dog('小红','狮子')
a.sayhi(weapon='刀')
a.sayhi()
print(a.name)
