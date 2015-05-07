#!usr/bin/env python
# -*-coding:utf-8 -*-


# os moudle http://www.cnblogs.com/BeginMan/p/3327291.html

import sys, string, os, shutil  
#输入目录名和前缀名，重命名后的名称结构类似prefix_0001  
def RenameFiles(srcdir, prefix):  
    if 0:
        srcfiles = os.listdir(srcdir)  
    else:
        srcfiles = os.listdir(os.getcwd())
        srcfiles = del_i(srcfiles)
        srcdir = os.getcwd()
    
    index = 1  
    for srcfile in srcfiles:  
        # 0 is the path 1 is the name , 2 is the sufix
        sufix = os.path.splitext(srcfile)[1]  
        #根据目录下具体的文件数修改%号后的值，"%04d"最多支持9999  
        destfile = srcdir + "//" + prefix + "_%04d"%(index) + sufix  
        srcfile = os.path.join(srcdir, srcfile)  
        os.rename(srcfile, destfile)  
        index += 1  

def del_i(lis):
    for na in lis:
        if na == 're_name.py':
            lis.remove(na)
    return lis



srcdir = "C://Users//Administrator//Desktop//python//train//batch rename//re"  
prefix = "DOCZ_2015"  
RenameFiles(srcdir, prefix)  