# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 10:13:22 2018

@author: zhulifu
"""

import tensorflow as tf
import matplotlib.pyplot as plt



image_raw_data_jpg = tf.gfile.FastGFile('C:/Users/zhulifu/Desktop/11.jpg', 'rb').read()
image_raw_data_png = tf.gfile.FastGFile('C:/Users/zhulifu/Desktop/1.jpg', 'rb').read()


a = tf.constant(12,tf.float32)
b = tf.constant(24,tf.float32)
sum = a+b

m = tf.placeholder(tf.float32)
n = tf.placeholder(tf.float32)
mn = m + n
add_trip = mn * 3

W = tf.Variable([.3],dtype = tf.float32)
b = tf.Variable([-.3],dtype = tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W*x + b

y = tf.placeholder(tf.float32)
squared_detals = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_detals)

fixW = tf.assign(W, [-1.])
fixb = tf.assign(b,[1.])

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

#################################################################################

init = tf.global_variables_initializer()
with tf.Session() as sess:
#sess = tf.Session()
    sess.run(init)
    print(sess.run(sum))
    print("a is :",sess.run(a))
    print(sess.run(b))
    
    print("Sessrun() is :",(sess.run(mn,{m:12,n:24})))
    print((sess.run(mn,{m:[1,3],n:[2,4]})))
    print("cheng ji si :",sess.run(add_trip,{m:12,n:24}))
    print(sess.run(linear_model,{x:[1,2,3,4]}))
    print(sess.run(loss,{x:[1,2,3,4],y:[0,1,2,3]}))
    
    sess.run([fixW,fixb])
    print(sess.run(loss, {x: [1,2,3,4,5], y: [0, -1, -2, -3,-4]}))
    
    for i in range(500):
        if i%100 ==0:
            sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})
            print("what is:",sess.run([W,b]),i)


    img_data_jpg = tf.image.decode_jpeg(image_raw_data_jpg) #图像解码 
    img_data_jpg = tf.image.convert_image_dtype(img_data_jpg, dtype=tf.uint8) #改变图像数据的类型 
      
    img_data_png = tf.image.decode_png(image_raw_data_png) 
    img_data_png = tf.image.convert_image_dtype(img_data_png, dtype=tf.uint8) 
      
    plt.figure(1) #图像显示 
    plt.imshow(img_data_jpg.eval()) 
    plt.figure(2) 
    plt.imshow(img_data_png.eval()) 
    plt.show() 
    
sess.close()
