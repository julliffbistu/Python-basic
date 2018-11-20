# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("MNIST_data/",one_hot = True)
keep_prob = tf.placeholder(tf.float32)
x = tf.placeholder(tf.float32,[None,784])

W = tf.Variable(tf.zeros([784,10]))

b = tf.Variable(tf.zeros([10]))

y_conv = tf.nn.softmax(tf.matmul(x,W) + b)

y_ = tf.placeholder(tf.float32,[None,10])
######################################################定义交叉熵
#cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y_conv))

cross_entropy = -tf.reduce_sum(y_*tf.log(y_conv))
########################################################
train_step = tf.train.AdamOptimizer(0.00001).minimize(cross_entropy)
#######################################################################
cross_prediction = tf.equal(tf.argmax(y_conv,1),tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(cross_prediction,"float"))

#init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(tf.global_variables_initializer())
#with tf.Session() as sess:
#sess.run(init)


for i in range(20000):
  batch = mnist.train.next_batch(50)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
  if i%100 == 0:
    train_accuracy = accuracy.eval(session=sess,
		feed_dict={x:batch[0], y_: batch[1], keep_prob: 1.0})
    print("step %d, training accuracy %g"%(i, train_accuracy))
  train_step.run(session=sess, feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
 
#输出最终的准确率
print("test accuracy %g"%accuracy.eval(session=sess, feed_dict={
    x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))

    
    
    
#    batch_xs,batch_ys = mnist.train.next_batch(100)
#    sess.run(train_step,feed_dict={x: batch_xs,y_: batch_ys})
#print (sess.run(accuracy,feed_dict={x: mnist.test.images,y_: mnist.test.labels}))








#sess = tf.InteractiveSession()
#tf.InteractiveSession.close()
#tf.global_variables_initializer().run()
#
#for _ in range(1000):
#    batch_xs,batch_ys = mnist.train.next_batch(100)
#    sess.run(train_step,feed_dict = {x:batch_xs,y_:batch_ys})
#correct_prediction = tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
#accuracy = tf.reduce_mean(tf.case(correct_prediction,tf.float32))
#print (sess.run(accuracy,feed_dict = {x:mnist.test.images,y_:mnist.test.labels}))

