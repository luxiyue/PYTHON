from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("input_data/",one_hot=True)
# print(mnist)
#784列 55000行 数据集
# print(mnist.train.images)
# print(mnist.train.labels)
#某个数字的 特征值
# print(mnist.train.images[0])
#获取50个图片的数据
print(mnist.train.next_batch(50))
#下面的数据 和 上面的不一样  获取的下一批50个
print(mnist.train.next_batch(50))