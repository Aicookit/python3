#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@qq.com
@software: garner
@file: 文件保存练习.py
@time: 2018/6/1/001 9:54
@desc:
'''
# w:写入，存在，就覆盖如不存在，就创建
# wb：二进制写入，存在，就覆盖如不存在，就创建
# w+:(读写，存在，就覆盖如不存在，就创建)
# wb+(二进制读写，存在，就覆盖如不存在，就创建)
# 相同的还有：r,rb(只读)、r+,rb+(读写)
# a:追加在结尾，存在，就覆盖，如不存在，就创建文件.a+(二进制)
# ab、ab+（二进制打开追加。。。）
# open()函数用于打开文件,有三个参数
# open(file,_mode,bufferingfile='缓冲大小')
# 介绍了stream流的概念：数据的流动方向，从内存流向外面，从计算机外面流向内存
#os模块还有对文件rename方法：os.rename('原文件格式'，'希望要的文件格式')
#删除文件方法：os.remove('文件')
#按行操作readline,readlines()
#文件迭代器
# import os
# f_name=open("E:\王者英雄.txt")
# for line in f_name:
#     print('line is:',line)
# f_name.close()
# import os
# try:
#     print('删除文件：',os.remove("E:\王者英雄'.jpg'"))
# except Exception:
#     print('文件不存在')

# import os
# file="E:\王者英雄\英雄.txt"
# f=open(file,'w')
# print(f.write('王昭君'))
# f.close()
###
# import os
# file="E:\王者英雄\英雄.txt"
# file="E:\王者英雄\英雄.txt"
# f=open(file,'a')
# print(f.write('和小强'))
# f.close()
# os.rename(file,"E:\王者英雄\英雄王昭君.txt")
#在txt格式的文件的正中央写一首诗
import os
import re
# file=open("E:\mypoem.txt",'w')
# file=open("E:\mypoem2.txt",'w')
# content='王者梦 君不见貂蝉妲己，\n草丛迎来刘备关羽。\n心待回城满血，\n天降赵云夺丝血。\n不论十八、八十岁，\n总有奇葩永相随。'
# print(file.write())
#文件目录创建
# import os
# # file=os.mkdir('E:\王者英雄\小英雄')
#
# file=os.makedirs('E:\王者英雄\小英雄1')
###我想把content（txt格式）保存进（打油诗）目录中
# content='王者梦 \n君不见貂蝉妲己，\n草丛迎来刘备关羽。\n心待回城满血，\n天降赵云夺丝血。\n不论十八、八十岁，\n总有奇葩永相随。'
# path='E:\打油诗'
# import os
# if not os.path.exists(path):
#     os.makedirs(path)            # 这里只创建了文件夹（壳）
# file_path=path + '/'+'王者梦.txt'    #这里创建了文件夹下的文件格式
# with open(file_path,'w') as f:        #这里打开了这个文件夹下的文件格式，并准备写入
#     f.write(content)                  #这里写入了实际内容
#     f.close()                     ----很成功！
###如果我想把（'姓名','很成功' ）这个元组拆开，把姓名建立成文件夹，把很成功建立成文件夹下的文本
# content=('姓名','很成功')
# path='E:\王者英雄'
# import os
# if not os.path.exists(path):
#     os.makedirs(path)
# file=path+'/'+content[0]+'.txt'
# with open(file,'w')as f:
#     f.write(content[1])
#     f.close()
###如果是列表呢？


