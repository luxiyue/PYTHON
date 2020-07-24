import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#固定值张量
# zero = tf.zeros([3,4],tf.float32)
# one = tf.ones([3,6],tf.float32)
# var = tf.constant(6.0,tf.float32)
# #随机张量
# # a = tf.random.normal([4,6],mean=2,stddev=1.0,dtype=tf.float32)
#
# #万能的类型转换公式(下面就是将int -> float)
# w = tf.cast([[1,2,3],[4,5,6]],tf.float32)
# with tf.Session() as sess:
#     print(zero.eval())
#     print(one.eval())
#     print(var.eval())
#     print(w.eval())



#变量的创建 op
#1.变量op能够持久化保存，普通张量Op是不行的
#2.当定义一个变量op的时候，一定要在会话当中去运行初始化
#3.name参数：在tensorboard使用的时候显示名字，可以让相同Op名字的进行区分
'''
tensorboard的使用：1.open in Terminal
                  2.tensorboard.exe --logdir="E:\文件\python\TenSor\heima\summary\test\events.out.tfevents.1594106493.LAPTOP-8JLCITUG"
 
'''
#先创建一个普通的张量
a = tf.constant([1,2,3,4,5])
var = tf.Variable(tf.random_normal([2,3],mean=0.0,stddev=1.0))
print(a,var)
#必须做一步显示的初始化
init_op = tf.global_variables_initializer()
with tf.Session() as sess:
    #必须运行初始化op
    sess.run(init_op)
    print(sess.run([a,var]))
    #将程序的图结构写入事件文件,graph:把指定的图写进事件文件当中，下面产生的文件作为可视化学习的一部分
    filewriter = tf.summary.FileWriter("summary/test/",graph=sess.graph)