# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 16:27:20 2018

@author: zhulifu
"""

import cv2
import numpy as np

def addsum(x,y):
    return x+y

def mutsum(x,y):
    return x*y

def plssum(x,y):
    return x-y

def oversum(x,y):
    return (x/y)

def yusum(x,y):
    return x%y

x1,y1 =0,0

def changedata(x,y):
    global x1,y1
    x1,y1 = y,x
    return x1,y1

def sum(x,y,data):
    if (data == 1):
        return x+y
    if (data == 2):
        return x-y
    if (data == 3):
        return x*y
    if (data == 4):
        return x/y
    if (data == 5):
        return x%y
    else:
        print("please input the correct data !")

def none():
    ceshi = 12
    print("the test is closing!")
    return ceshi

a,b= 12,4
changnumber = changedata(a,b)
print('a and b change end data is :',x1,y1)
print("the add data is :",addsum(a,b))
print("the mut data is :",mutsum(a,b))
print("the pls data is :",plssum(a,b))
print("the over data is :",oversum(a,b))
print("the yu data is :",yusum(a,b+1))
print("________________________________________________________________________")
print("the add  is :",sum(a,b,1))
print("the mut  is :",sum(a,b,2))
print("the pls  is :",sum(a,b,3))
print("the over  is :",sum(a,b,4))
print("the yu  is :",sum(a,b+1,5))
print("the yu  is :",sum(a,b+1,34))
none()
end = 2*none()
print("end",end)

def printstr(str):
    print(str)
    a = 2
    return a
#    return

str = ' ai ya wo ca !'
printstr(str)
x = 2 * printstr(str)
print(x)

def printinfo(arg1,*vartuple):
    print("输出：")
    print(arg1)
    
    for var in vartuple:
        print(var)
    return

printinfo(10,1,1,23,688,34,56,23,45656)


def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50,34,56,43 )

def add(a,b,*,c):
    return a+b+c

end_data = add(1,2,c = 3)
print(add(1,2,c = 3))

if (end_data == 4):
    print("the data is right")
else:
    print("data error")

if True:
    smg = 4
    
print("smg is :",smg)

############局部变量和全局变量##########################
# =============================================================================
total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
 
#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)
# =============================================================================

###########如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，
#########如下实例：##
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()





