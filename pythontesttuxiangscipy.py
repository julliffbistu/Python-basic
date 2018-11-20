# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 14:57:50 2018

@author: zhulifu
"""
from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters

im = array(Image.open('1.jpg').convert('L'))
im2 = filters.gaussian_filter(im,5)
#imshow(im2)


#im = array(Image.open('1.jpg'))
#im2 = zeros(im.shape)
#for i in range(3):
#    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],5)
#im2 = uint8(im2)
#imshow(im2)
#im2 = array(im2,'uint8')

img = array(Image.open("1.jpg").convert('L'))

imx = zeros(img.shape)
filters.sobel(img,1,imx)

imy = zeros(im.shape)
filters.sobel(img,1,imy)

magnitude = sqrt(imx**2 + imy**2)

sigma =5
immx = zeros(img.shape)
filters.gaussian_filter(img,(sigma,sigma),(0,1),immx)

immy = zeros(img.shape)
filters.gaussian_filter(img,(sigma,sigma),(1,0),immy)

subplot(2,2,1)
imshow(imx)
title('x')
subplot(2,2,2)
imshow(imy)
title('y')
subplot(2,2,3)
imshow(immx)
title('mx')
subplot(2,2,4)
imshow(immy)
title('my')

figure()
from scipy.ndimage import measurements,morphology
# 载入图像，然后使用阈值化操作，以保证处理的图像为二值图像
im = array(Image.open('11.jpg').convert('L'))
im = 1*(im<128)
labels, nbr_objects = measurements.label(im)
print ("Number of objects:", nbr_objects)



im_open = morphology.binary_opening(im,ones((9,5)),iterations=2)
labels_open, nbr_objects_open = measurements.label(im_open)
print ("Number of objects:", nbr_objects_open)



def denoise(im,U_init,tolerance=0.1,tau=0.125,tv_weight=100):

    m,n = im.shape # 噪声图像的大小
    # 初始化
    U = U_init
    Px = im # 对偶域的 x 分量
    Py = im # 对偶域的 y 分量
    error = 1
    while (error > tolerance):
        Uold = U
    GradUx = roll(U,-1,axis=1)-U # 变量 U 梯度的 x 分量
    GradUy = roll(U,-1,axis=0)-U # 变量 U 梯度的 y 分量
    # 更新对偶变量
    PxNew = Px + (tau/tv_weight)*GradUx
    PyNew = Py + (tau/tv_weight)*GradUy
    NormNew = maximum(1,sqrt(PxNew**2+PyNew**2))
    Px = PxNew/NormNew # 更新 x 分量（对偶）
    Py = PyNew/NormNew # 更新 y 分量（对偶）
    # 更新原始变量
    RxPx = roll(Px,1,axis=1) # 对 x 分量进行向右 x 轴平移
    RyPy = roll(Py,1,axis=0) # 对 y 分量进行向右 y 轴平移
    DivP = (Px-RxPx)+(Py-RyPy) # 对偶域的散度
    U = im + tv_weight*DivP # 更新原始变量
    # 更新误差
    error = linalg.norm(U-Uold)/sqrt(n*m);
    return U,im-U # 去噪后的图像和纹理残余
# 使用噪声创建合成图像
im = zeros((500,500))
im[100:400,100:400] = 128
im[200:300,200:300] = 255
im = im + 30*random.standard_normal((500,500))
U,T = rof.denoise(im,im)
G = filters.gaussian_filter(im,10)
# 保存生成结果
from scipy.misc import imsave
imsave('synth_rof.pdf',U)
imsave('synth_gaussian.pdf',G)
imshow(U)

im = array(Image.open('11.jpg').convert('L'))
U,T = rof.denoise(im,im)
figure()
gray()
figure()
imshow(U)
axis('equal')
axis('off')
show()






