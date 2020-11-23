#对demo5的改进
#coding=utf-8
from multiprocessing import Queue

if __name__ == '__main__':
    q = Queue(3)  #初始化一个Queue对象，最多可接收3条put消息
    q.put("消息 1")
    q.put("消息 2")
    print(q.full()) #返回false
    q.put("消息 3")
    print(q.full())  #返回true、

    #因为消息队列已满，下面的try都会抛出异常
    #第一个try会等待2s后再抛出异常，第二个try会立刻抛出异常
    try:
        q.put("消息4",True,2)
    except:
        print("消息队列已满，现有消息量：%s"%q.qsize())

    try:
        q.put_nowait("消息4")
    except:
        print("消息队列已满，现有消息量：%s"%q.qsize())

    #读取消息时，先判断消息队列是否为空，再读取
    if not q.empty():
        print("-----从列表中获取消息-----")
        for i in range(q.qsize()):
            print(q.get_nowait())


    #先判断消息队列是否已满，再写入
    if not q.full():
        q.put_nowait("消息4")

    
    
