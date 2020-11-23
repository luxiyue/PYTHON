import threading,time

def process():
    for i in range(3):
        time.sleep(1)
        print("thread name is %s" % threading.current_thread().name)


if __name__ == '__main__':
    print("----主线程开始-----")
    threads = [threading.Thread(target=process) for i in range(4)]#创建4个线程，存入列表
    for t in threads:
        t.start()  #开启线程
    for t in threads:
        t.join()   #等待子线程结束
    print("----主线程结束----")
