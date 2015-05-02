#!usr/bin/env python
#-*- coding:utf-8

import random2
import string



strings=''

'''
for i in range(0,10):
	string+=str(int(i))
for i in range(97,123):
	string+=chr(int(i))
'''
#generate 'abcdef.....XYZ'
strings=string.letters
#generate '01234..9'
for i in range(65,91):
	strings+=chr(int(i))


#random2.choice() picks up a letter from strings
#\r\n is to changer row
def gener_num(leng):
	l_num=''
	for i in range(0,leng):
		l_num+=random2.choice(strings)
	l_num+='\r\n'
	return l_num

def file_write():

	'''
	fp = open("result.txt",'ab')
	string = gener_num(9)
	fp.write(string)  
	fp.close() 
	'''

	with open("result.txt",'ab') as fp:
		strs = gener_num(10)
		fp.write(strs)


if __name__ == '__main__':
	for n in range(0,10):
		file_write()

