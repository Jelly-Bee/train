#!/usr/bin/env python
# encoding: utf-8

import Image,ImageDraw,ImageFont

orign_pic='avatar.png'
result_pic='new_avatar.png'

def add_num(add_text):
	fp=Image.open(orign_pic)
	height,width=fp.size
	font=ImageFont.truetype('arial.ttf',(height/4))

	dr=ImageDraw.Draw(fp)

	dr.text((height*0.75,0),add_text,fill=(255,0,0),font=font)

	fp.show()
	fp.save(result_pic)

if __name__=='__main__':
	add=raw_input('please enter number:')
	add_num(add)




