# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:07:22 2018

@author: zhulifu
"""

from PIL import Image
import matplotlib.pyplot as plt
import os

pil_image= Image.open('1.jpg')
#pil_image.show()
plt.figure("picture")
plt.imshow(pil_image)
plt.show()

pil_im = pil_image.convert('L')
#pil_im = Image.open('1.jpg').convert('L')
plt.figure("picture 1")
plt.imshow(pil_im)
plt.show()

#for infile in filelist:
#    outfile = os.path.splitext(infile)[0] + ".jpg"
#    if file !=outfile:
#        try:
#            Image.open(infile).save(outfile)
#        except IOError:
#            print("cannot convert",infile)

box = (100, 100, 400, 400)
pil_img = pil_im.crop(box)
plt.figure("picture2")
plt.imshow(pil_img)
plt.show()

pil_img = pil_img.transpose(Image.ROTATE_180)
pil_img.paste(pil_img,box)
plt.figure("picture3")
plt.imshow(pil_img)
plt.show()

outimg = pil_img.resize((480,480))
plt.figure("picture4")
plt.imshow(outimg)
plt.show()

outimg1 = pil_img.rotate(45)
plt.figure("picture4")
plt.imshow(outimg1)
plt.show()











