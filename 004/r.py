# -*- coding: utf-8 -*-

import re

def count(filepath):
    f = open(filepath, 'rb')
    s = f.read()
    words = re.findall(r'[a-zA-Z0-9\-]+', s)
    return len(words)

if __name__ == '__main__':
    num = count('git.txt')
    print num

'''
 {m.n}用来表示前面正则表达式的m到n次copy,尝试匹配尽可能多的copy。
   >>> re.findall("a{2,4}","aaaaaaaa")
　['aaaa', 'aaaa']
'''
 #reference site re moudle  http://blog.sina.com.cn/s/blog_a15aa56901017liq.html
 #http://www.cnblogs.com/sevenyuan/archive/2010/12/06/1898075.html
 #http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832260566c26442c671fa489ebc6fe85badda25cd000
 #  ****** http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html