#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@qq.com
@software: garner
@file: 面向对象.py
@time: 2018/5/17/017 16:16
@desc:
'''
# 创建一个类
# class myClass:
#     i=12345                     #定义的变量
#     def f(self):                #定义的函数
#         return 'hello world'
# x=myClass()                     #实例化这个类
# print(x.i)                      #打印类里面的属性
# print(x.f())                    #打印类里面的函数

# 创建一个类，并把它实例化
# class people:
#     name='person'
#     __age= 24
    # _sex= '男'
#
# x=people()
# # xiaoming=people()
# # dadong=people()
# # print(dadong.name)
# # print(xiaoming.name)
# print(x.__age)
# print(x._sex)
'''
类的方法和函数
'''
#构造函数（初始化方法）
# class Recetage():
#     def __init__(self):
#         self.weidth=0
#         self.heigth=0
#     def setsize(self,size):
#         self.weidth=size
#         self.heigth=size
#     def getsize(self):
#         return self.weidth,self.heigth
#         size=property(get.heigth,get.weidth)
# class Bird:
#
#     def voice(self):
#         print('叽叽唧唧')
#     def fly(self):
#         print('I can fly in the sky')
#
# class Duck(Bird):
#     def __init__(self,more_words):
#         print('I can',more_words)
# dc=Duck('呱呱')
#
# huangli=Bird()
# huangli.voice()
# huangli.fly()

# class Test:
#     def __init__(self,name):
#         self.name=name
#     # def say(self):
#     #     print('hello from ' +self.name +' !')
#     def say(me):
#         print('hello from '+ me.name+ ' !')
# me=Test('kity')
# me.say()

# def db_conn():
#     print("connecting db")
# def db_backup(dbname):
#     print('导出数据库...',dbname)
#     print('将备份打包，移至相关目录...')
# def db_backup_test():
#     print('将备份导入测试库，看是否成功')
#
# def main():
#     db_conn()
#     db_backup('dbname')
#     db_backup_test()
#
# if __name__=='__main__':
#     main()

# 面向对象实战
#定义四个人，两红方：妲己，关羽，两蓝方：孙膑，兰陵王
# 分别有血量，攻击力，金钱，我们可以把人物属性放在一个字典里，方便后续调用
# role={
# 1:
# {'name':'妲己',
#  'blood':1000,
#  'atk':90,
#  'money':300
# },
# 2:
# {'name':'关羽',
#  'blood':1100,
#  'atk':115,
#  'money':300
# },
# 3:
# {'name':'孙膑',
#  'blood':1200,
#  'atk':70,
#  'money':300
# },
# 4:
# {'name':'兰陵王',
#  'blood':900,
#  'atk':120,
#  'money':300
# },
# }
# # print(role[2])
# '''
# 角色的基本属性设计后，接下来为每个角色开发以下几个功能:
# 被攻击后就会掉血的功能
#
# 。。。
# 我们可以把每个功能写成一个函数，类似如下：
# '''
# def get_atk(who):
#     pass#减少血量
#     who['blood']-=10
# def buy(who):
#     pass#购买，减金钱，加攻击
#     who['money']-=250
#     who['atk']+= 50
# def move():
#     pass
#
#                         #精简版
# class Role(object):
#     def __init__(self,name,role,weapon,life_value=1000):
#         self.name=name
#         self.role=role
#         self.weapon=weapon
#
#     def atk(self):
#         print('我打...')
#
#     def get_atk(self,haha,tong):
#         print('哎哟...',haha,tong)
#
#     def buy_gun(self,gun_name):
#         print('just bought %s （枪名）'%gun_name)
#
# # r1=Role('关羽','战士','偃月刀',115)        #生成一个角色
# # r2=Role('刘备','文人','雨伞',90)
# # r2.get_atk(haha=2,tong=3)
# # r1.buy_gun('偃月刀')                      #这个角色做了什么事？方法函数
# print(type(Role))
'''
项目描述
1、创建一个学校成员类，这个类登记成员的姓名并在成员加入时自我介绍，还要统计学校的总人数。
2、创建一个老师类，这个类继承学校成员类，创建对象的时候总人数加一，老师类重写具体打招呼的类容
3、创建一个学生类，这个继承学校成员类，创建对象时总人数也会加一，学生类重写打招呼的类容，增加一个方法介绍自己的学习情况。
4、实例对象结束的时候，总人数减一
'''
# class SchoolMember(object):
#     members=0
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def add_normal_member_say(self,teachers_choose):
#         print('hello,I am new here! my name is %s.'%self.name,teachers_choose)
#     def add_teacher_say(self):
#         print('Hello,i am your teacher!i am %s'%self.name)
#     def enrool(self):
#         SchoolMember.members += 1
#         print('new member [%s] is enrolled,now there is [%d] members'%(self.name,SchoolMember.members))
    # def __del__(self):
    #     # 析构方法
    #     print('%s is happy'%self.name)
#2.定义老师类
# class Teacher(SchoolMember):
#     def __init__(self,name,age):
#         super(Teacher,self).__init__(name,age)
#         self.name=name
#         self.age=age
#         # self.course=course
#         # self.salary=salary
#     def teacher_say(self):
#         print('hello,everyone,I love you!I am %s老师'%self.name)
#     def count_teacher(self):
#         SchoolMember.members += 1
#         print('加上这位%s老师，现在总人数是%d个'%(self.name,SchoolMember.members))

#定义学生类
# class Student(SchoolMember):
#
# teacher3=Teacher('小王',5)
# teacher3.teacher_say()
# teacher3.count_teacher()
#定义学生
# studentA=SchoolMember('小明',18)
# studentA.add_normal_member_say('i like beautiful teacher')
# studentA.enrool()
# teacher1=SchoolMember('王老师',35)
# teacher1.add_teacher_say()
# teacher1.enrool()
# # teacher2=SchoolMember('赵刚',45,)
# # teacher2.add_normal_member_say('I like you guys')
###面向对象之构造函数
# class Myinit(object):
#     def __init__(self,name):
#         self.name=name
#     def myfunction(self):
#         print('this is my first function')
# if __name__ == '__main__':
#     it=Myinit('小明')
#     print(it.name)

''''
类的相关方法：

类的相关方法(定义一个类,也会产生自己的名称空间)
类名.__name__   # 类的名字(字符串)
类名.__doc__    # 类的文档字符串
类名.__base__   # 类的第一个父类(在讲继承时会讲)
类名.__bases__  # 类所有父类构成的元组(在讲继承时会讲)
类名.__dict__   # 类的字典属性、名称空间
类名.__module__ # 类定义所在的模块
类名.__class__  # 实例对应的类(仅新式类中)
'''
# > class students(object):
# ...     count=0
# ...     def __init__(self,name,age):
# ...             self.name=name
# ...             self.age=age
# ...             students.count += 1
# ...
# >>> if __name__== "__main__":
# ...     xiaoming=students('xiaoming',122)
# ...     print(xiaoming.__dict__)
# ...     student2=students('dadong',111)
# ...     print(student2.__dict__)
# ...     print(students.count)
#
# {'name': 'xiaoming', 'age': 122}
# {'name': 'dadong', 'age': 111}
# 2


