#普通的神经网络
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

FLAGS = tf.app.flags.FLAGS
#1为训练 0为测试
tf.app.flags.DEFINE_integer("is_train",0,"指定程序是预测还是训练")

def full_connected():

    #获取真实的数据
    mnist = input_data.read_data_sets("input_data/",one_hot=True)

    #1、建立数据的占位符 x[None，784] y_true [None,10]
    with tf.variable_scope("data"):
        x = tf.placeholder(tf.float32,[None,784])
        y_true = tf.placeholder(tf.int32,[None,10])

    #2.建立一个全连接层的神经网络（只有一层） w[784,10] b[10]
    with tf.variable_scope("fc_model"):
        # 随机初始化权重和偏置
        weight = tf.Variable(tf.random_normal([784,10],mean=0.0,stddev=1.0,name="w"))
        bias = tf.Variable(tf.constant(0.0,shape=[10]))
        #预测None个样本的输出结果matrix[None,784] * [784,10] + [10] = [None,10]
        y_predict = tf.matmul(x,weight) + bias

    #3、求出所有样本的损失，然后求平均值
    with tf.variable_scope("soft_cross"):
        #求平均交叉熵损失 tf.reduce_mean:求列表的平均值
        loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_true,logits=y_predict))

    #4.梯度下降求出损失
    with tf.variable_scope("optimizer"):
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    #5.计算准确率
    with tf.variable_scope("acc"):
        equal_list = tf.equal(tf.argmax(y_true,1),tf.argmax(y_predict,1))
        # equal_list None个样本  [1,0,1,0,1,1,.....]
        accuracy = tf.reduce_mean(tf.cast(equal_list,tf.float32))

    # #收集变量 单个数字收集
    # tf.summary.scalar("losses",loss)
    # tf.summary.scalar("acc",accuracy)
    # #高纬度变量变量收集
    # tf.summary.histogram("weightes",weight)
    # tf.summary.histogram("biases",bias)

    #定义一个合并变量的OP
    # merged = tf.summary.merge_all()

    #定义一个初始化的OP
    init_op = tf.global_variables_initializer()

    #创建一个saver
    saver = tf.train.Saver()

    #6.开启会话去训练
    with tf.Session() as sess:
        #初始化变量
        sess.run(init_op)
        if FLAGS.is_train == 1:
            #迭代步骤去训练
            for i in range(10000):
                #取出真实存在的特征值和目标值
                mnist_x,mnist_y = mnist.train.next_batch(500)
                #建立events文件 然后写入
                # filewriter = tf.summary.FileWriter("summary/test/",graph=sess.graph)
                #运行train_op训练
                sess.run(train_op,feed_dict={x:mnist_x,y_true:mnist_y})
                # 写入每步训练的值
                # summary = sess.run(merged,feed_dict={x:mnist_x,y_true:mnist_y})
                # filewriter.add_summary(summary,i)
                print("训练第%d步，准确率为：%f" % (i+1,sess.run(accuracy,feed_dict={x:mnist_x,y_true:mnist_y})))
            #保存模型
            saver.save(sess,"model/fc_model")
        else:
            #加载模型
            if os.path.exists("model/checkpoint"):
                saver.restore(sess,"model/fc_model")
            # 如果是0，做出预测
            for i in range(100):
                #x_test:特征值  y_test:目标值
                x_test,y_test = mnist.test.next_batch(1)
                print("第%d张图片，数字目标是%d,预测结果是：%d" % (
                    i+1,
                    tf.argmax(y_test,1).eval(),
                    tf.argmax(sess.run(y_predict,feed_dict={x:x_test,y_true:y_test}),1).eval()
                ))

    return None

if __name__ == '__main__':
    full_connected()