#读取狗图片
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


def picread(filelist):
    """
    读取图片并转换成张量
    ：param filelist:文件路径 + ，名字的列表
    ：return :每张图片的张量
    """
    #1.构造文件的队列
    file_queue = tf.train.string_input_producer(filelist)
    #2.构造阅读器读取队列数据
    reader = tf.WholeFileReader()
    key,value = reader.read(file_queue)
    #对读取的图片数据进行解码
    image = tf.image.decode_jpeg(value)
    print(image)
    #4.处理图片的大小（统一大小）
    image_resize = tf.image.resize_images(image,[200,200])
    print(image_resize)

    #注意一定要把样本的形状固定 [200,200,3],在批处理的时候要求所有数据形状必须定义
    image_resize.set_shape([200,200,3])

    #5.进行批处理 4张图片 1个线程
    image_batch = tf.train.batch([image_resize],batch_size=4,num_threads=1,capacity=4)
    print(image_batch)
    return image_batch

if __name__ == '__main__':
    #找到文件，放入列表 路径+名字 -》 列表
    file_name = os.listdir("dog/")
    file_list = [os.path.join("dog/",file) for file in file_name]
    image_batch = picread(file_list)
    #开启会话运行结果
    with tf.Session() as sess:
        #定义一个线程协调器
        coord = tf.train.Coordinator()
        #开启读文件的线程
        threads = tf.train.start_queue_runners(sess,coord=coord)
        #打印读取的内容
        print(sess.run([image_batch]))
        #回收子线程
        coord.request_stop()
        coord.join(threads)