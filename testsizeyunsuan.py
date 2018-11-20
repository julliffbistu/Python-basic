# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 08:56:40 2018

@author: zhulifu
"""

import tensorflow as tf
import numpy as np

a = tf.constant(3.0)
b = tf.constant(4.0)

c = tf.constant([2.0,2.0])
d = tf.constant([2.0,3.0])

t1 = tf.add(a,b)
t2 = tf.add(c,d)

t3 = tf.div(a,b)
t4 = tf.div(c,d)

t5 = tf.less(a,b)
t6 = tf.less(c,d)

t7 = tf.greater(a,b)
t8 = tf.greater(c,d)

t9 = tf.equal(a,b)
t10 = tf.equal(c,d)

with tf.Session() as sess:
    sess.run(t1)
    print("t1:",sess.run(t1),"\n")
    sess.run(t2)
    print("t2:",sess.run(t2),"\n")
    sess.run(t3)
    print("t3:",sess.run(t3),"\n")
    sess.run(t4)
    print("t4:",sess.run(t4),"\n")
    sess.run(t5)
    print("t5:",sess.run(t5),"\n")
    sess.run(t6)
    print("t6:",sess.run(t6),"\n")
    sess.run(t7)
    print("t7:",sess.run(t7),"\n")
    sess.run(t8)
    print("t8:",sess.run(t8),"\n")
    sess.run(t9)
    print("t9:",sess.run(t9),"\n")
    sess.run(t10)
    print("t10:",sess.run(t10),"\n")
############################################################################################################################
print("###############################____________________########################################___________________#######")
m = [[1,2,3],[4,5,6]]
n= tf.constant([[2,3,4],[5,6,7]])


x = tf.shape(m)
y = n.get_shape()
with tf.Session() as sess:
    print(sess.run(tf.rank(m)))
    print(sess.run(tf.rank(n)))
    print(x)
    print(sess.run(x))
    print(y)
#    print(sess.run(shuffle(m)))

############################################################################################################################
print("_______________________________________________________________________________________________________________")


a1 = tf.constant([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0], shape=[3,3],dtype = tf.float64)
a2 = tf.constant([2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],shape = [3,3],dtype = tf.float64)
print(a1)
print(a2)

a1a2 = tf.matmul(a1,a2)
a1ni = tf.matrix_inverse(a1a2)
a1nizheng = tf.cast(a2,dtype = tf.float64)
sum = tf.matrix_determinant(a1)
print("sum",sum)

aaa = tf.constant([1, 2, 3, 4],shape=[2,2],dtype=tf.float64) 
z = tf.matrix_determinant(a1)





init = tf.global_variables_initializer()
with tf.Session() as sess:
    print("\na1 is :",sess.run(a1),"\na2 is :",sess.run(a2),"\na1a2 is :",sess.run(a1a2))
    print("\na1ni is :\n",sess.run(a1ni))
    print("\a1nizheng is :\n",sess.run(a1nizheng))
    print("\nsum is :\n",sess.run(z))














