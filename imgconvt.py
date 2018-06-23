#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@gmail.com
@software: garner
@file: imgconvt.py
@time: 2018/5/2/002 16:03
@desc:
'''
from PIL import Image

def get_chars(pi):
    chars = [' ', ',', '1', '+', 'n', 'D', '@', 'M']
    for k in range(0, 8):
        if pi < (k + 1) * 32:
            return chars[7 - k]

def imgsave(imgName,data):
    fi = open(imgName + '.txt', 'w')
    for d in data:
        print(d, file=fi)
    fi.close()

if __name__=='__main__':
    imgName='E:\images/u.jpg'
    img=Image.open(imgName)
    imgconvt=img.convert('L')
    w,h=imgconvt.size
    if w>100:
        h=int((100/w)*h)
        w=100
        a=imgconvt.resize((w,h),Image.ANTIALIAS)
    # 下面我想把缩小的图片中的像素值用符号替换并保存列表
    data=[]
    for i in range(0,h):
        line = ''
        for j in range(0,w):
            pi = a.getpixel((j,i))
            line +=get_chars(pi)
    data.append(line)

# 查看颜色像素值范围
# a.getpixel((w,h))
# 正式替换/
# 输出保存/
imgsave(imgName,data)

print('convert success1')