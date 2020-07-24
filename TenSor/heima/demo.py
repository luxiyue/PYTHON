import tensorflow as tf
#下面两行代码的作用是去掉 ’加速警告‘
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#op:只要使用tensorflow的API定义的函数都是OP
#tensor: 就指代的是数据

#创建一张图
# g = tf.Graph()
# print(g)
# with g.as_default():
#     c = tf.constant(11.0)
#     print(c.graph)


#实现一个加法运算
#下面的不叫变量，叫张量（tensor）
a = tf.constant(5.0)
b = tf.constant(6.0)

# print(a,b)#发现打印的不是值 而是个类型
sum1 = a+b
# print(sum1)#也不是值
sum2 = tf.add(a,b)


#默认的这张图，相当于是给程序分配一段内存
# graph = tf.get_default_graph()
# print(graph)

#普通变量
var1 = 2.0
#tensor对象
var2 = var1 + sum1


#训练模型
#实时的提供数据去进行训练
#placeholder是一个占位符，free_dict一个字典
# plt = tf.placeholder(tf.float32,[2,3])
plt = tf.placeholder(tf.float32,[None,3])#None表示填的行不固定
#只能运行一个图，可以在会话中指定图取执行
# with tf.Session(config=tf.ConfigProto(log_device_placement=True)) as sess:#config作用是打印运行的细节
with tf.Session() as sess:
    # print( sess.run(plt,feed_dict={plt:[[1,2,3],[4,5,6]]} ) )
    # 普通的变量不能运行！
    # print(sess.run(var1))
    #但是普通变量和tensor变量加减后的变量 默认就是tensor
    # print(sess.run(var2))
    # print(sess.run(sum1))
    # print(sess.run([a,b,sum1]))
    # print(sum1.eval())
    # print(sess.run(sum2))
    # #你会发现图的地址=都是相同的
    # print(a.graph)
    # print(sum1.graph)
    # print(sess.graph)
    # print(a.shape)
    # print("="*100)
    # print(plt.shape)
    # print("=" * 100)
    # print(a.name)
    # print("="*100)
    # print(a.op)
    pass


#tensorflow：打印出来的形状表示
#0维：()    1维：(5)     2维:(5,6)
'''静态形状：创建一个张量，初始化静态形状'''
#tf.Tensor.get_shape:获取静态形状
#tf.Tensor.set_shape:更新Tensor对象的静态形状
plt = tf.placeholder(tf.float32,[None,2])
print(plt)
plt.set_shape([3,2])
print(plt)
#对于静态形状来说，一旦张量形状固定了，不能再次设置静态形状,所以下面的一行代码会报错  并且上面的set_shape 如果修改为[3,1]也会报错因为列是2已经固定了
# plt.set_shape([2,3])
# print(plt)

'''动态形状：一种描述原始张量在执行过程中的一种形状（动态变化）'''
#tf.reshape:创建一个具有不同动态形状的新张量
plt_reshape = tf.reshape(plt,[1,6])#记住行和列的乘积必须和原来的行列乘积相等
print(plt_reshape)


