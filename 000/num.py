#!/usr/bin/env python
# encoding: utf-8

"""
第 0000 题：将你的 QQ 头像（或者微博头像）右上角加上红色的数字，
类似于微信未读信息数量那种提示效果。 类似于图中效果

Image gets the stream
ImageDraw gets the Draw stream
ImageFont modifies the font type; 

若提示错误，重装PIL

"""

import Image,ImageDraw,ImageFont

orign_pic='avatar.png'
result_pic='new_avatar.png'

def add_num(add_text):
	#getstream
	fp=Image.open(orign_pic)
	height,width=fp.size
	#get font 
	font=ImageFont.truetype('arial.ttf',(height/4))
	#get draw stream
	dr=ImageDraw.Draw(fp)
	#text(xy,text,color,font)
	dr.text((height*0.75,0),add_text,fill=(255,0,0),font=font)

	fp.show()
	fp.save(result_pic)

if __name__=='__main__':
	add=raw_input('please enter number:')
	add_num(add)




