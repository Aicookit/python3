#!/usr/bin/env python3
# encoding: utf-8
'''
@author: itcoo
@license: (C) Copyright 2017-2019, Node Supply Chain Manager Corporation Limited.
@contact: 642250219@qq.com
@software: garner
@file: 自制表情包.py
@time: 2018/6/5/005 21:02
@desc:
'''
from PIL import Image,ImageDraw,ImageFont

img1=Image.open('E:\images/1.png')
img1.resize((500,500),Image.ANTIALIAS)
img2=Image.open('E:\images/f.jpg')
img1.paste(img2,(105,95))
draw=ImageDraw.Draw(img1)
ttfront=ImageFont.truetype('f.jpg',24)
draw.text((73,20),'361装逼卫士',fill=(238,92,13),font=ttfront)
draw.text((40,220),'让你多一度安全装逼',fill=(0,0,0),font=ttfront)
img1.show( )