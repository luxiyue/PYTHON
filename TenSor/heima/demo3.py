#这篇代码只是展示  同步模拟的过程

import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#模拟一下同步先处理数据，然后才能去数据训练
#tensorflow当中，运行操作有依赖性

#1.首先定义队列
Q = tf.FIFOQueue(3, tf.float32)
#放入一些数据
enq_many = Q.enqueue_many([[0.1,0.2,0.3],])  #如果只写[0.1,0.2,0.3] 则不会被当成张量

#2.定义一些读取数据，取数据的过程     取数据，+1  入队列
out_q = Q.dequeue()
data = out_q + 1
en_q = Q.enqueue(data)


with tf.Session() as sess:
    #初始化队列
    sess.run(enq_many)
    #处理数据
    for i in range(2):
        sess.run(en_q)#因为tensorflow有依赖性，所以执行该行代码会默认执行上面另外的两条代码
    #训练数据
    for i in range(Q.size().eval()):
        print(sess.run(Q.dequeue()))
