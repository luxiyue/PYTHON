#使用队列在线程中通信

from queue import Queue
import random,threading,time

#生产者
class Producer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data = queue
    def run(self):
        for i in range(5):
            print("生产者%s将产品%d加入队列！"%(self.getName(),i))
            self.data.put(i)
            time.sleep(random.random())
        print("生产者%s完成！"%self.getName())


#消费者类
class Consumer(threading.Thread):
    def __init__(self,name,queue):
        threading.Thread.__init__(self,name=name)
        self.data = queue
    def run(self):
        for i in range(5):
            val = self.data.get()
            print("消费者%s将产品 %d 加入队列！" % (self.getName(),val))
            time.sleep(random.random())
        print("消费者%s完成！"%self.getName())

if __name__ == '__main__':
    print("-----主线程开始-----")
    queue = Queue()
    #创建两个线程类
    producer = P+roducer("Producer",queue)
    consumer = Consumer("Consumer",queue)
    #执行子线程
    producer.start()
    consumer.start()
    #等待子线程执行
    producer.join()
    consumer.join()
    print("-----主线程结束-----")