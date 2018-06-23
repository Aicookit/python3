#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@gmail.com
@software: garner
@file: 项目集.py
@time: 2018/5/16/016 21:59
@desc:
'''
'''
猜数字游戏，增加一些有趣的功能和效果：
1、计算机在所设定的范围内随机生成一个数，作为被猜数。
2、每猜一个数，计算机首先判断在不在所设定的范围：如果不在，提示用户重新输入；如果在，提示用户新的数字范围。
3、增加有趣的互动语句，请尽情发挥吧。
'''
# 导入用到的随机生成数的库
import random
print('欢迎来到猜数字游戏')

while 1:
    print('(注意：确定请输入1，退出请输入2)')
    choose=input('请选择1或者2：')
    choose=int(choose)

    if choose == 1:
        computer=random.randint(1,10)

        while choose:
            guess=input('请说出你觉得对的数字（在1-10中选出一个）：')
            guess=int(guess)            #python3中input（）函数输入的是字符串
            if guess < computer:
                print('你猜小了，请大胆一点！')
            elif guess > computer:
                print('你猜大了，再小一些！')
            elif guess == computer:
                print('恭喜，这么快就猜到了！')
                break           #遇到的问题：如何退出到外部循环？

    elif choose ==2:
        print('游戏结束！')
        break

    else:
        print('没有这个选项哦，请重新开始！')
        break
