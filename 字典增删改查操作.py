#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@qq.com
@software: garner
@file: 字典增删改查操作.py
@time: 2018/5/19/019 11:40
@desc:
'''
'''
如何进行字典列表的增删改查操作和显示全部信息?以建立名片为形式，以name,sex,age,address为字典内容。
例：[{'name':'li','sex':'male','address':'china'},{'name':'li','age':16,'address':'china'}]
'''

card_file=[]                     #建立名片夹

print('='*50)
print('恭喜您成功打开名片文件夹'+' '*29+'*')
print('输入1,增添内容。'+' '*35+'*')
print('输入2,删除内容。'+' '*35+'*')
print('输入3,改换内容。'+' '*35+'*')
print('输入4,查找内容。'+' '*35+'*')
print('输入5,全部内容。'+' '*35+'*')
print('输入6,退出！   '+' '*35+'*')
print('='*50)

card={}                 #single 名片
#增加内容
choose=input('请输入要进行的操作数字：')    #记住：python3中input的内容是字符串！
choose=int(choose)
if choose == 1:                         #选1，进行增加内容操作
    new_name = input('输入要添加的名字：')
    new_age=input('输入要添加的年龄：')
    new_addr = input('输入要添加的地址：')
    new_card={}
    new_card['name']=new_name
    new_card['age'] = new_age
    new_card['addr'] = new_addr
    card_file.append(new_card)
    print(card_file)                                            #定义一个新字典，装新内容
    continue               #for test
else:
    break
    print('请重新开始！')








# if choose == 2:
# if choose == 3:
# if choose == 4:
# if choose == 5:
# if choose == 6:








