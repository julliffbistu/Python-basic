# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:29:48 2018

@author: zhulifu
"""

from PIL import Image
import numpy as np
from pylab import *

img = array(Image.open('1.jpg'))
#imshow(img)

print(img.shape,img.dtype)

img2 = array(Image.open('1.jpg').convert('L'),'f')
#img2 = array(Image.open('1.jpg').convert('L'),'f')
print(img2.shape,img2.dtype)

img3 = 255 - img2
#imshow(img3)

img4 = (100.0/255)*img3 + 100


img5 = 255.0 * (img3/255.0)**2
#imshow(img5)
print (int(img5.min()),int(img5.max()))

pil_im = Image.fromarray(img5) ##fanxiang
#imshow(pil_im)

def imresize(im,sz):
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

img6 = imresize(img5,(img5.shape[1]//2,img5.shape[0]//2))
#imshow(img6)

def histeq(im,nbr_bins = 256):
    imhist,bins=histogram(im.flatten(),nbr_bins,normed = True)
    cdf = imhist.cumsum()
    cdf= 255 * cdf / cdf[-1]
    im2 = interp(im.flatten(),bins[:-1],cdf)
    return im2.reshape(im.shape),cdf

im7,cdf = histeq(img6)
imshow(im7)
title('niubi')
for i in range(8):
    subplot(2,4,i+1)
    imshow(im7)
    








