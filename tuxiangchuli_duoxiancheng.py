# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:56:51 2018

@author: zhulifu
"""
"""
import cv2
import threading
import numpy as np
from time import ctime,sleep

def thread_1():
    print("The thread_1 time is %s \n" %ctime())
    img1 = cv2.imread('1.jpg')
    img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    _,img1_bin = cv2.threshold(img1_gray,150,255,cv2.THRESH_BINARY)
    cv2.imshow("IMG1",img1_bin)
    cv2.waitKey(10000)
    return
    
    
def thread_2():
    print("The thread_2 time is %s \n" %ctime())
    img2 = cv2.imread('11.jpg')
    img2_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    _,img2_bin = cv2.threshold(img2_gray,150,255,cv2.THRESH_BINARY)
    cv2.imshow("IMG2",img2_bin)
    cv2.waitKey(10000)
    return
    
threads = []
t1 = threading.Thread(target = thread_1)
threads.append(t1)
t2 = threading.Thread(target = thread_2)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
#    t.join()  ##等待子进程是否结束
###主线程########################
    print("The main thread time is %s \n" %ctime())
    img3 = cv2.imread('lena3.jpg')
    cv2.imshow("img3",img3)
    cv2.waitKey(10000)
    
cv2.destroyAllWindows()
"""


###############################################################################
print("-----------------多线程子线程返回结果给主线程----------------------------")

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 15:56:51 2018

@author: zhulifu
"""

"""
import cv2
import threading
import numpy as np
from time import ctime,sleep

#img1_bin = np.zeros([600,600,3],dtype=np.uint8)
#img2_bin = np.zeros([600,600,3],dtype=np.uint8)

def thread_1():
    global img1_bin
    print("The thread_1 time is %s \n" %ctime())
    img1 = cv2.imread('1.jpg')
    img1_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    _,img1_bin = cv2.threshold(img1_gray,150,255,cv2.THRESH_BINARY)
#    cv2.imshow("IMG1",img1_bin)
#    cv2.waitKey(10000)
    return img1_bin
    
    
def thread_2():
    global img2_bin
    print("The thread_2 time is %s \n" %ctime())
    img2 = cv2.imread('11.jpg')
    img2_gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    _,img2_bin = cv2.threshold(img2_gray,150,255,cv2.THRESH_BINARY)
#    cv2.imshow("IMG2",img2_bin)
#    cv2.waitKey(10000)
    return img2_bin
    
threads = []
t1 = threading.Thread(target = thread_1)
threads.append(t1)
t2 = threading.Thread(target = thread_2)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()  ##等待子进程是否结束
###主线程########################
    print("The main thread time is %s \n" %ctime())
    img3 = cv2.imread('lena3.jpg')
    
    cv2.imshow("IMG1",img1_bin)
    cv2.imshow("IMG2",img2_bin)
    cv2.imshow("img3",img3)
    cv2.waitKey(10000)
    
cv2.destroyAllWindows()
"""

###############################################################################
print("-----------------多线程子线程返回结果给主线程--死循环---------------------")






























