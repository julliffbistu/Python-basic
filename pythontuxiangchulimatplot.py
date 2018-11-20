# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:05:20 2018

@author: zhulifu
"""

from PIL import Image
from pylab import *

img = array(Image.open('1.jpg'))
#plt.figure("picture")
#plt.imshow(img)
#plt.show()

imshow(img)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

plot(x,y,'ks:')

plot(x[:4],y[:4])

title('Plotting:"empire.jpg"')
#axis('off')
show()

imggray = array(Image.open('1.jpg').convert('L'))
imshow(imggray)

figure()
gray()

contour(imggray,origin = 'image')
axis('equal')

figure()
hist(imggray.flatten(),128)
show()

#figure()
#imgbiao = array(Image.open('1.jpg'))
#imshow(imgbiao)
#
#print("please click 3 pionts")
#
#x = ginput(3)
#print("you click point is :",x)
#show()









