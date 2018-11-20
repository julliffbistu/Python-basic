# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:45:06 2018

@author: zhulifu
"""

import cv2
import numpy as np
K = 1

def chuli1(img,img_out):
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _ ,img_out = cv2.threshold(img1,150,255,cv2.THRESH_BINARY)
    return img_out

def  chuli2(img1,img1_out):
    global K
    green = (0,215,0)
    cv2.line(img1,(200,20),(200,400),green,8)
    
    (centerx,centery) = (img1.shape[1]//2,img1.shape[0]//2)
    white = (221,19,23)
    for r in range(0,175,25):
        cv2.circle(img1,(centerx,centery),r,white,4)
    img1_out = img1
    K = 20
    return img1_out
        

cap = cv2.VideoCapture(0)
while(1):
    ret,frame = cap.read()
    frame_out = np.array(frame)  ###########关键定义成numpy数组######
#    frame_out_out = np.array(frame)
    img3 = chuli1(frame,frame_out)
    img4 = chuli2(frame_out,frame_out)
    KK = 10*K
    print("KK")
    cv2.imshow("frame",img4)
    if cv2.waitKey(30) & 0xff == 32:
        break
cap.release()
cv2.destroyAllWindows()





