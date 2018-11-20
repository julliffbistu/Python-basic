# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:21:47 2018

@author: zhulifu
"""

from OpenGL.GL import *
from OpenGL.GLU import *
import pygame, pygame.image
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def drawFunc():
    # 清楚之前画面
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1, 5, 5, 0)  # (角度,x,y,z)
    glutWireTeapot(0.5)
    # 刷新显示
    glFlush()


# 使用glut初始化OpenGL
glutInit()
# 显示模式:GLUT_SINGLE无缓冲直接显示|GLUT_RGBA采用RGB(A非alpha)
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
# 窗口位置及大小-生成
glutInitWindowPosition(0, 0)
glutInitWindowSize(1000, 1000)
glutCreateWindow(b"first")
# 调用函数绘制图像
glutDisplayFunc(drawFunc)
glutIdleFunc(drawFunc)
# 主循环
glutMainLoop()


def set_projection_from_camera(K):

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    fx = K[0,0]
    fy = K[1,1]
    fovy = 2*arctan(0.5*height/fy)*180/pi
    aspect = (width*fy)/(height*fx)
    
    near = 0.1
    far = 100.0
    
    # 设定透视
    gluPerspective(fovy,aspect,near,far)
    glViewport(0,0,width,height)

def set_modelview_from_camera(Rt):
    
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    #  围绕 x 轴将茶壶旋转 90 度，使 z 轴向上
    Rx = array([[1,0,0],[0,0,-1],[0,1,0]])
    #  获得旋转的最佳逼近
    R = Rt[:,:3]
    U,S,V = linalg.svd(R)
    R = dot(U,V)
    R[0,:] = -R[0,:] # 改变 x 轴的符号
    # 获得平移量
    t = Rt[:,3]
    # 获得 4×4 的模拟视图矩阵
    M = eye(4)
    M[:3,:3] = dot(R,Rx)
    M[:3,3] = t
    # 转置并压平以获取列序数值
    M = M.T
    m = M.flatten()
    # 将模拟视图矩阵替换为新的矩阵
    glLoadMatrixf(m)

def draw_background(imname):
    # 载入背景图像（应该是 .bmp 格式），转换为 OpenGL 纹理
    bg_image = pygame.image.load(imname).convert()
    bg_data = pygame.image.tostring(bg_image,"RGBX",1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # 绑定纹理
    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D,glGenTextures(1))
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,width,height,0,GL_RGBA,GL_UNSIGNED_BYTE,bg_data)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_fiLTER,GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_fiLTER,GL_NEAREST)
    # 创建四方形填充整个窗口
    glBegin(GL_QUADS)
    glTexCoord2f(0.0,0.0); glVertex3f(-1.0,-1.0,-1.0)
    glTexCoord2f(1.0,0.0); glVertex3f( 1.0,-1.0,-1.0)
    glTexCoord2f(1.0,1.0); glVertex3f( 1.0, 1.0,-1.0)
    glTexCoord2f(0.0,1.0); glVertex3f(-1.0, 1.0,-1.0)
    glEnd()
    # 清除纹理
    glDeleteTextures(1)

from OpenGL.GLUT import *
glutSolidTeapot(size)
def draw_teapot(size):
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glClear(GL_DEPTH_BUFFER_BIT)
    # 绘制红色茶壶
    glMaterialfv(GL_FRONT,GL_AMBIENT,[0,0,0,0])
    glMaterialfv(GL_FRONT,GL_DIFFUSE,[0.5,0.0,0.0,0.0])
    glMaterialfv(GL_FRONT,GL_SPECULAR,[0.7,0.6,0.6,0.0])
    glMaterialf(GL_FRONT,GL_SHININESS,0.25*128.0)
    glutSolidTeapot(size)


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pygame, pygame.image
from pygame.locals import *
import pickle
width,height = 1000,747
def setup():
    
    pygame.init()
    pygame.display.set_mode((width,height),OPENGL | DOUBLEBUF)
    pygame.display.set_caption('OpenGL AR demo')
# 载入照相机数据
with open('ar_camera.pkl','r') as f:
    K = pickle.load(f)
    Rt = pickle.load(f)
    setup()
    draw_background('11.jpg')
    set_projection_from_camera(K)
    set_modelview_from_camera(Rt)
    draw_teapot(0.02)
while True:
   event = pygame.event.poll()
   if event.type in (QUIT,KEYDOWN):
       break
pygame.display.flip() 
print("end")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    