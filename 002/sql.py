#!usr/bin/env python
# -*-coding:utf-8 -*-

import MySQLdb
import r_n

def connt_db(val):
    conn = MySQLdb.connect(host='localhost',user='root',passwd='password')
    curs = conn.cursor()
    conn.select_db('mid')
    #不为NULL
    if val == '':
        return
    valu = []
    valu.append(val)
    print valu
    #the valu must be a list
    curs.execute("insert into ser values(%s)",valu)
    conn.commit()
    conn.close()
    curs.close()

def write_code():
    with open('result.txt') as fp:
        for line in fp:
            #用来删除换行符
            line = line.strip('\r\n')
            connt_db(line)


if __name__ == '__main__':
	#connt_db()
    write_code()

#reference site http://my.oschina.net/davehe/blog/128361
