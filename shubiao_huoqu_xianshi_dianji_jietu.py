# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Fri Nov 16 10:51:55 2018
# 
# @author: zhulifu
# """
# import cv2
# import numpy as np
# drawing = False
# mode = True
# start = (-1,-1)
# 
# #############单个点点击############################
# # =============================================================================
# # def mouse_event_one(event,x,y,flags,param):  ###定义鼠标返回函数
# #     if event == cv2.EVENT_LBUTTONDOWN:###左键按下
# #         print((x,y))
# #         juge_data = 1
# # =============================================================================
# #    return juge_data
#         
# def mouse_event(event,x,y,flags,param):
#     global start,drawing,mode
#     ###按下左键
#     if event == cv2.EVENT_LBUTTONDOWN:
#         drawing = True
#         start(x,y)
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if drawing:
#             if mode:
#                 cv2.rectangle(img,start,(x,y),(0,255,0),4)
#             else:
#                 cv2.circle(img,(x,y),5,(0,0,255),4)
#                 
#     ####左键释放
#     elif event == cv2.EVENT_LBUTTONUP:
#         drawing = False
#         if mode:
#             cv2.rectangle(img,start,(x,y),(0,255,0),4)
#         else:
#             cv2.circle(img,(x,y),5,(0,0,255),4)
#             
#     
# 
# img = np.zeros((512, 512, 3), np.uint8)
# cv2.namedWindow('image1')
# cv2.setMouseCallback('image1', mouse_event)
# 
# 
# 
# cap = cv2.VideoCapture(0)  ##VideoCapture
# while(True):
#     ret,frame = cap.read()
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     _,thredhold = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
#     
#     cv2.namedWindow('image')
#     cv2.setMouseCallback('image', mouse_event)
# #    if juge_data == 1:
# #        font=cv2.FONT_HERSHEY_SIMPLEX
# #        cv2.putText(frame,"opencv",(100,300),font,4,(255,0,255),2)
#     
#     cv2.imshow('image1', img)
#     cv2.imshow("image",frame)
#     if cv2.waitKey(1) == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()
# =============================================================================

# -*- coding: utf-8 -*-
#############################点击鼠标留一个圈#####################
# =============================================================================
# import cv2
# import numpy as np
# 
# 
# def draw_circle(event, x, y, flags, param):
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         cv2.circle(img, (x, y), 20, (255, 0, 0), -1)
# 
# 
# # =============================================================================
# # img = np.zeros((512, 512, 3), np.uint8)
# # cv2.namedWindow('image')
# # cv2.setMouseCallback('image', draw_circle)
# # =============================================================================
# cap = cv2.VideoCapture(0)
# img =np.zeros((512, 512, 3), np.uint8)
# while True:
#     ret,frame = cap.read()
#     cv2.namedWindow('image')
#     cv2.setMouseCallback('image', draw_circle)
#     cv2.imshow('image', img)
#     
#     
#     
#     cv2.imshow("frame",frame)
#     if cv2.waitKey(20) & 0xff == 32:
#         break
# cap.release()
# cv2.destroyAllWindows()
# =============================================================================

# -*- coding: utf-8 -*-

import cv2
import numpy as np


#当鼠标按下时变为 True
drawing = False
#如果mode为True绘制矩形， 按下m变成绘制曲线
mode = True
ix, iy = -1, -1

#创建回调函数
def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode
    #当按下左键时返回起始点坐标
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    #当鼠标按下并移动时绘制图形，可以查看移动，flag是否按下
    elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 4)
            else:
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

    #当鼠标松开时停止绘画
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)
while True:
    cv2.imshow('image', img)
#    cv2.imshow("frame",frame)
    if cv2.waitKey(20) & 0xff == 32:
        break
cap.release()
cv2.destroyAllWindows()








































