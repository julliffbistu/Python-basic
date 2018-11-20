# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:28:51 2018

@author: zhulifu
"""
from PIL import Image
import numpy as np
from scipy import ndimage
from pylab import *

def normalize(points):
    for row in points:
        row /= points[-1]
    return points

def make_homog(points):
    return vstack((points,ones((1,points.shape[1]))))

def H_from_points(fp,tp):
    if fp.shape != tp.shape:
        raise RuntimeError('number of points do not match')
    m = mean(fp[:2],axis = 1)
    maxstd = max(std(fp[:2],axis = 1)) + 1e-9
    C1 = diag([1/maxstd,1/maxstd,1])
    C1[0][2] = -m[0]/maxstd
    C1[1][2] = -m[1]/maxstd
    fp = dot(C1,fp)
    
    m = mean(tp[:2], axis=1)
    maxstd = max(std(tp[:2], axis=1)) + 1e-9

    C2 = diag([1/maxstd, 1/maxstd, 1])
    C2[0][2] = -m[0]/maxstd
    C2[1][2] = -m[1]/maxstd
    tp = dot(C2,tp)
    # 创建用于线性方法的矩阵，对于每个对应对，在矩阵中会出现两行数值
    nbr_correspondences = fp.shape[1]
    A = zeros((2*nbr_correspondences,9))
    for i in range(nbr_correspondences):
        A[2*i] = [-fp[0][i],-fp[1][i],-1,0,0,0,
          tp[0][i]*fp[0][i],tp[0][i]*fp[1][i],tp[0][i]]
        A[2*i+1] = [0,0,0,-fp[0][i],-fp[1][i],-1,
          tp[1][i]*fp[0][i],tp[1][i]*fp[1][i],tp[1][i]]
    U,S,V = linalg.svd(A)
    H = V[8].reshape((3,3))
    # 反归一化
    H = dot(linalg.inv(C2),dot(H,C1))
    # 归一化，然后返回
    return H / H[2,2]

def Haffine_from_points(fp,tp):

    if fp.shape != tp.shape:
        raise RuntimeError('number of points do not match')
    # 对点进行归一化
    # --- 映射起始点 ---
    m = mean(fp[:2], axis=1)
    maxstd = max(std(fp[:2], axis=1)) + 1e-9
    C1 = diag([1/maxstd, 1/maxstd, 1])
    C1[0][2] = -m[0]/maxstd
    C1[1][2] = -m[1]/maxstd
    fp_cond = dot(C1,fp)
    # --- 映射对应点 ---
    m = mean(tp[:2], axis=1)
    C2 = C1.copy() # 两个点集，必须都进行相同的缩放
    C2[0][2] = -m[0]/maxstd
    C2[1][2] = -m[1]/maxstd
    tp_cond = dot(C2,tp)
    # 因为归一化后点的均值为 0，所以平移量为 0
    A = concatenate((fp_cond[:2],tp_cond[:2]), axis=0)
    U,S,V = linalg.svd(A.T)
    # 如 Hartley 和 Zisserman 著的 Multiple View Geometry in Computer ,  Scond Edition 所示，
    # 创建矩阵 B 和 C
    tmp = V[:2].T
    B = tmp[:2]
    C = tmp[2:4]
    tmp2 = concatenate((dot(C,linalg.pinv(B)),zeros((2,1))), axis=1)
    H = vstack((tmp2,[0,0,1]))
    #  反归一化
    H = dot(linalg.inv(C2),dot(H,C1))
    return H / H[2,2]

im = array(Image.open('11.jpg').convert('L'))
figure()
imshow(im)
H = array([[1.4,0.05,-100],[0.05,1.5,-100],[0,0,1]])
im2 = ndimage.affine_transform(im,H[:2,:2],(H[0,2],H[1,2]))
figure()
gray()
imshow(im2)
show()


def image_in_image(im1,im2,tp):
# 扭曲的点
    m,n = im1.shape[:2]
    fp = array([[0,m,m,0],[0,0,n,n],[1,1,1,1]])
    # 计算仿射变换，并且将其应用于图像 im1
    H = Haffine_from_points(tp,fp)
    im1_t = ndimage.affine_transform(im1,H[:2,:2],
    (H[0,2],H[1,2]),im2.shape[:2])
    alpha = (im1_t > 0)
    return (1-alpha)*im2 + alpha*im1_t

im1 = array(Image.open('1.jpg').convert('L'))
im2 = array(Image.open('11.jpg').convert('L'))
# 选定一些目标点
tp = array([[264,538,540,264],[40,36,605,605],[1,1,1,1]])
im3 = image_in_image(im1,im2,tp)
figure()
gray()
imshow(im3)
axis('equal')
axis('off')
show()

def alpha_for_triangle(points,m,n):
    alpha = zeros((m,n))
    for i in range(min(points[0]),max(points[0])):
        for j in range(min(points[1]),max(points[1])):
            x = linalg.solve(points,[i,j,1])
            if min(x) > 0: #  所有系数都大于零
                alpha[i,j] = 1
    return alpha



m,n = im1.shape[:2]
fp = array([[0,m,m,0],[0,0,n,n],[1,1,1,1]])
#  第一个三角形
tp2 = tp[:,:3]
fp2 = fp[:,:3]
#  计算 H
H = Haffine_from_points(tp2,fp2)
im1_t = ndimage.affine_transform(im1,H[:2,:2],
                                 (H[0,2],H[1,2]),im2.shape[:2])
#  三角形的 alpha
alpha = alpha_for_triangle(tp2,im2.shape[0],im2.shape[1])

im3 = (1-alpha)*im2 + alpha*im1_t
# 第二个三角形
tp2 = tp[:,[0,2,3]]
fp2 = fp[:,[0,2,3]]
# 计算 H
H = Haffine_from_points(tp2,fp2)
im1_t = ndimage.affine_transform(im1,H[:2,:2],
                                 (H[0,2],H[1,2]),im2.shape[:2])
# 三角形的 alpha 图像
alpha = alpha_for_triangle(tp2,im2.shape[0],im2.shape[1])
im4 = (1-alpha)*im3 + alpha*im1_t
figure()
gray()
imshow(im4)
axis('equal')

show()

import matplotlib.delaunay as md
x,y = array(random.standard_normal((2,100)))
centers,edges,tri,neighbors = md.delaunay(x,y)
figure()
for t in tri:
    t_ext = [t[0], t[1], t[2], t[0]] # 将第一个点加入到最后
    plot(x[t_ext],y[t_ext],'r')
plot(x,y,'*')
axis('off')
show()





    