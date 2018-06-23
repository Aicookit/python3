#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@gmail.com
@software: garner
@file: imgconvert1.py
@time: 2018/5/6/006 22:51
@desc:
'''
from PIL import Image
# 打开图片地址
imagewr='E:\images/1.png'
image=Image.open(imagewr)
# 转换为灰度图片
img=image.convert('L')
# 缩小尺寸
w,h=img.size
# print((w,h))
# 等比例缩小
if w>100:
    h=int((100/w)*h)
    w=100
imge=img.resize((w,h))
# imge.show()为缩小后的图片
imge.save('E:\images/qq.jpg')
# 将灰度图片（0，255）的颜色值转化成字符
data=[]
# 用八个字符替代颜色值
chars=[' ',',','1','+','n','D','@','M']
# 开始循环遍历颜色取值
for i in range(0,h):
    line=''
    for j in range(0,w):
        pixel=imge.getpixel((i,j))
        # print(pixel)
        # 将灰度图片颜色值转换为字符
        for k in range(0,8):
            if pixel<((k+1)*32):
                line +=chars[7-k]
    data.append(line)
# print(data)
f=open('E:\images/'+'2q.txt','w')
for d in data:
    print(d,file=f)
f.close()
print('convert success')



