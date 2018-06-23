#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@gmail.com
@software: garner
@file: play_loop.py
@time: 2018/5/11/011 17:20
@desc:
'''
# me='renyingming666'
# i=0
# while i < len(me):
#     print(me[i])
#     i += 1
# else:
#     print('条件顺利执行')

me='renyingming666'
# for i in me:
# #     print(i)
# 获取下标对应的值
# for (i,v) in enumerate(me):
#     print(i,v)
#     if i == 10:
#         break
# else:
#     print('完成输出')

# 使用for和while计算1到100之间奇数的和
# for

# total=0
# for i in range(1,101):
#     if i%2 != 0:
#         total += i
# print(total)

# while
# sum = 0
# num = 1
# while num <= 100:
#     if num%2 != 0:
#         sum += num
#     num += 1
# print(sum)

# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
# 程序分析：isalpha方法判断是否是字母，isspace方法判断是否是空格，isdigit方法判断是否是数字
# chars='ab bcdefg 123_&*'
# digit_count = 0
# alpha_count=0
# space_count=0
# else_count = 0
# for i in chars:
#     if i.isdigit():
#         digit_count+=1
#     elif i.isalpha():
#         alpha_count+=1
#     elif i.isspace():
#         space_count+=1
#     else:
#         else_count+=1
# print('此字符串中有字母%s个，空格%s个，数字%s个，特殊字符%s个。'%(alpha_count,space_count,digit_count,else_count))

# print(alpha_count,space_count,digit_count,else_count)


    # count=0
    # if i.isalpha():
    #     alpha_count =count+1
    # elif i.isspace():
    #     space_count=count+1
    # elif i.isdigit():
    #     digit_count=count+1
# 猜数字游戏项目
import random    #引入库，生成随机数
print('welcome to the guess number game!')

while 1:                    #循环1，选择‘1，确定’和‘2 结束’按钮，进入和退出游戏
    print("                      '-确定-'  \n                      '-取消-' ")
    tem=input('确定请按1，结束请按2：')
    tem=int(tem)
    if tem == 1:
        print('开始游戏')
        temp=random.randint(1,16)

        while tem:
            guess=input('在1-16中猜个号码试试：')
            guess=int(guess)
            if guess < temp:
                print('小了小了，再来一次，要大一点的')
            elif guess > temp:
                print('大了大了，再来一次，要小一点的')
            elif guess == temp:
                print('你真棒，竟然猜对了')
                break
            else:
                break

    elif tem == 2:
        print('游戏结束')
        break
    else:
        print("亲，可没这个选项！")









