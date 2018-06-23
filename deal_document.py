#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@gmail.com
@software: garner
@file: deal_document.py
@time: 2018/5/14/014 17:12
@desc:
'''
# 文件处理和异常
# file=open('my_document.txt','w',encoding='utf-8')#打开文件或创建
# file.write('hello,I\'m itcoo')#写入内容
# file.close()#关闭
# 2with...as...方法
# with open('my_document.txt','r+',encoding='utf-8') as file:
# #     file.write("i used 'with...as' way here.")
# #     print(file.readline())
# print('i'+'\n'+'love'+'\n'+'you')换行符的使用‘\n’
# 实战项目：把用户输入的东西保存在创建的文件里,如果用户输入‘quit’or‘exit’则退出
# 用户一直在输入，就要使用循环，使用while True
# while True:
#     document=input('用户输入：')
#     if document in ['quit','exit']:#if write == 'quit' or write == 'exit':
#         break
#     with open('user_document.txt','a+',encoding='utf-8') as f:
#         f.write(document+'\n')
# 把用户输入的信息在控制台console中遍历出来显示
# while True:
#     document=input('用户输入：')
#     if document in ['quit', 'exit']:
#         with open('user_Document.txt','r',encoding='utf-8') as f:#33,34,35行功能是把写好的文件再显示出来
#             for v in f:
#                 print(v,end='')
#         break
#     with open('user_Document.txt','a',encoding='utf-8') as f:
#         f.write(document+'\n')
# 异常
# try:
# #     int('abcd')
# # except ValueError as e:
# #     print('error solved')
# # else:
# #     print('no error')
# # finally:
# #     print('dont care the error,always execute coding')
'''
1、计算机在所设定的范围内随机生成一个数，作为被猜数。
2、每猜一个数，计算机首先判断在不在所设定的范围：如果不在，提示用户重新输入；如果在，提示用户新的数字范围。
3、增加有趣的互动语句，请尽情发挥吧。
'''








