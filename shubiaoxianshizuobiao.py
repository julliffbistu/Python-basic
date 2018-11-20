# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 14:37:33 2018

@author: zhulifu
"""

# =============================================================================
import cv2
import numpy as np
from PIL import Image,ImageDraw,ImageFont

x1,y1 = 0,0

def mouse_event(event,x,y,flags,param):
    global x1,y1
    if event == cv2.EVENT_MOUSEMOVE:
#        print(x,y)
        x1,y1 = x,y
        
        
cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_event) 
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    print(x1,y1)
    cv2.circle(frame,(x1,y1),5,(0,0,255),4)
    
    font=cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'('+str(x1) +',' + str(y1)+')',(x1,y1),font,2,(255,0,255),2)
#    cv2.putText(frame,str(y1),(x1+150,y1),font,2,(255,0,255),2)
    
    
    frame = Image.fromarray(frame)
    draw = ImageDraw.Draw(frame)
    font = ImageFont.truetype("simhei.ttf",40,encoding="utf-8")#参数1：字体文件路径，参数2：字体大小；Windows系统“simhei.ttf”默认存储在路径：C:\Windows\Fonts中
    draw.text((100,0),"中科院自动化所",(255,0,0),font=font)
    frame = cv2.cvtColor(np.array(frame),cv2.COLOR_RGB2BGR)
    
    green = (0,215,0)
    cv2.line(frame,(x1+50,y1+50),(x1+200,y1+50),green,8)
    
    cv2.imshow("image",frame)
    if cv2.waitKey(20) & 0xff == 32: ##cv2.waitKey(20) == ord('32'):
        break
cap.release() 
cv2.destroyAllWindows()  
# =============================================================================

# =============================================================================
# import cv2
# 
# global img
# global point1, point2
# def on_mouse(event, x, y, flags, param):
#     global img, point1, point2
#     img2 = img.copy()
#     if event == cv2.EVENT_LBUTTONDOWN:         #左键点击
#         point1 = (x,y)
#         cv2.circle(img2, point1, 10, (0,255,0), 5)
#         cv2.imshow('image', img2)
#     elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):               #按住左键拖曳
#         cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
#         cv2.imshow('image', img2)
#     elif event == cv2.EVENT_LBUTTONUP:         #左键释放
#         point2 = (x,y)
#         cv2.rectangle(img2, point1, point2, (0,0,255), 5) 
#         cv2.imshow('image', img2)
#         min_x = min(point1[0],point2[0])     
#         min_y = min(point1[1],point2[1])
#         width = abs(point1[0] - point2[0])
#         height = abs(point1[1] -point2[1])
#         cut_img = img[min_y:min_y+height, min_x:min_x+width]
#         cv2.imwrite('11_jie.jpg', cut_img)
# 
# def main():
#     global img
#     img = cv2.imread('11.jpg')
#     cv2.namedWindow('image')
#     cv2.setMouseCallback('image', on_mouse)
#     cv2.imshow('image', img)
#     cv2.waitKey(1000)
# 
# if __name__ == '__main__':
#     main()
# 
# =============================================================================

