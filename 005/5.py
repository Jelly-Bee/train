#!/usr/bin/env python
# encoding: utf-8

# referecne site PIL  http://zhan.renren.com/hopeinmind?gid=3602888498036325669&checked=true
# glob  http://blog.csdn.net/csapr1987/article/details/7469769
# os module http://www.cnblogs.com/BeginMan/p/3327291.html


from PIL import Image
import glob

def get_list():
	#return list
	return glob.glob(r'./*.jpg')

def image_process(image_name):
	im = Image.open(image_name)
	(x_r,y_r) = im.size
#按比例调整大小
	if x_r > y_r:
		x_s = 640
		y_s = y_r * x_s / x_r
	else:
		y_s = 1136
		x_s = x_r * y_s / y_r
	im2 = im.resize((x_s,y_s))
	im2.save(image_name+'_new.jpg','jpeg')

def change():
	img_list = get_list()
	for li in img_list:
		image_process(li)


if __name__ == '__main__':
			change()
