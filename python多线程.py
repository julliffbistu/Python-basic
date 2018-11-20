# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 13:12:08 2018

@author: zhulifu
"""



import numpy as np
import threading
from time import ctime,sleep

def music():
    for i in range(2):
        print("I was listen to music. %s" %ctime())
        sleep(1)
        
def move():
    for i in range(2):
        print("I was at the movies! %s" %ctime())
        sleep(5)
        
if __name__ == '__main__':
    music()
    move()
    print("all over time is : %s" %ctime())

###############################################################################
print("-----------------------------1111---------------------------------------")
import numpy as np
import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print("I was listen to %s. %s" %(func,ctime()))
        sleep(1)
        
def move(func):
    for i in range(2):
        print("I was at the %s! %s" %(func,ctime()))
        sleep(5)
        
if __name__ == '__main__':
    music(u'爱情买卖')
    move(u'taitannikehao')
    print("all over time is : %s" %ctime())
    

###############################################################################
print("--------------------------22222-----------------------------------------")

import numpy as np
import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print("I was listen to %s. %s" %(func,ctime()))
        sleep(4)
        
def move(func):
    for i in range(2):
        print("I was at the %s! %s" %(func,ctime()))
        sleep(5)
        
threads = []
t1 = threading.Thread(target = music,args = (u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target = move,args = (u'taitannikehao',))
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
####setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起
        t.setDaemon(True)
        t.start()

### join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。     
    t.join()
    print("all over time is %s" %ctime())

###创建是颇为麻烦的，每创建一个线程都需要创建一个tx（t1、t2、...），如果创建的线程多时候这样极其不方便。
###############################################################################
    

print("--------------------------33333-----------------------------------------")
import numpy as np
import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print("I was listen to %s. %s" %(func,ctime()))
        sleep(2)
        
def move(func):
    for i in range(2):
        print("I was at the %s! %s" %(func,ctime()))
        sleep(5)

def player(name):
    r = name.split('.')[1]  ##以’.‘分成2片，【1】是指第二个元素的索引（index）
    if r == 'mp3':
        music(name)
    else:
        if r == 'mp4':
            move(name)
        else:
            print("The format is not recongnized !")


list = ['爱情买卖.mp3','taitannikehao.mp4','伟大的爱.mp4']
threads = []
files = range(len(list))

for i in files:
    t = threading.Thread(target = player,args = (list[i],))
    threads.append(t)
    
if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
        
    print("end time is %s" %ctime())
   
###############################################################################
    
    
print("--------------------------44444-----------------------------------------")
import threading
from time import sleep,ctime

def super_player(file,time):
    for i in range(2):
        print("start playing : %s! %s" %(file,ctime()))
        sleep(time)
        
####播放列表和播放时长######################
list = {'爱情买卖.mp3':3,'afanti.mp4':5,'我不知道.mp4':4,'想起来mp3':2}
threads = []
files = range(len(list))

for file,time in list.items():
    t = threading.Thread(target = super_player, args=(file,time))
    threads.append(t)
    
if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
    
    ##主线程##
    print("The end time is %s"%ctime())
    

###############################################################################
    
    
print("--------------------------多线程类-------------------------------------")
import threading
from time import sleep,ctime

class MyThread(threading.Thread):
    
    def __init__(self,func,args,name = ''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
        
    def run(self):
        self.func(*self.args)  ##Python3 
#        apply(self.func,self.args)  ##Python2
        
def super_player(file,time):
    for i in range(2):
        print("start playing %s! %s" %(file,ctime()))
        sleep(time)
        
list = {'爱情买卖.mp3':3,'afanti.mp4':5,'我不知道.mp4':4,'想起来mp3':2}

threads = []
files = range(len(list))

for k,v in list.items():
    t = MyThread(super_player,(k,v),super_player.__name__)
    threads.append(t)
    
if __name__ == '__main__':
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()
        
######主线程####################
    print("The end time is %s"%ctime())
    
















