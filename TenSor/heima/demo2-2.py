import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



def myregression():#其实下面的代码不需要with tf.variable_scope  也行，他的目的是使得结构更加清晰
    """
    自实现一个线性回归预测
    ：return:None
    """
    with tf.variable_scope("data"):
        #1.准备数据，x 特征值[100,1] y 目标值[100]
        x = tf.random_normal([100,1],mean=1.75,stddev=0.5,name="x_data")
        #矩阵相乘必须是二维的
        y_true = tf.matmul(x,[[0.7]]) + 0.8

    with tf.variable_scope("model"):
        #2.建立线性回归模型 1个特征，1个权重  一个偏置 y=xw+b
        #随机给一个权重和偏置的值，让他去计算损失，然后在当前状态下优化
        #Trainable:指定这个变量能跟着梯度下降一起优化 默认为True  如果为False，则训练时不会改变
        weight = tf.Variable(tf.random_normal([1,1],mean=0.0,stddev=1.0),name="W",trainable=True)#用变量定义才能优化
        bias = tf.Variable(0.0,name="b")
        y_predict = tf.matmul(x,weight) + bias

    with tf.variable_scope("loss"):
        # 3.建立损失函数，均方误差
        loss = tf.reduce_mean(tf.square(y_true - y_predict))

    with tf.variable_scope("optimizer"):
        #4.梯度下降优化损失  learning_rate:0~1 2 3 4 5 6 7 10
        train_op = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    #收集tensor
    tf.summary.scalar("losses",loss)
    tf.summary.histogram("weights",weight)
    #定义合并tensor的op
    merged = tf.summary.merge_all()

    #定义一个初始化变量的op
    init_op = tf.global_variables_initializer()

    #定义一个保存模型的实例
    saver = tf.train.Saver()

    #通过会话运行程序
    with tf.Session() as sess:
        #初始化变量
        sess.run(init_op)
        #打印随机最先初始化的权重和偏zhi
        print("随机初始化的参数权重为：%f,偏置为：%f" % (weight.eval(),bias.eval()) )
        #循环训练 运行优化
        #建立事件文件
        filewriter = tf.summary.FileWriter("summary/test/",graph=sess.graph)

        #加载模型,覆盖模型当中随机定义的参数，从上次训练的参数结果开始
        if os.path.exists("ckpt/checkpoint"):
            saver.restore(sess,"ckpt/model")

        for i in range(500):
            sess.run(train_op)
            #运行合并的tensor
            summary = sess.run(merged)
            filewriter.add_summary(summary,i)

            if i%20==0:
                print("第%d次参数权重为：%f,偏置为：%f" % (i,weight.eval(), bias.eval()))
        saver.save(sess,"ckpt/model")

    return None

if __name__ == '__main__':
    myregression()