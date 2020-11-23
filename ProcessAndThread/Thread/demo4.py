#使用互斥锁
from threading import Thread,Lock
import time


n=100  #共100张票

def task():
    global n
    mutex.acquire()   #上锁
    temp = n          #赋值给临时变量
    time.sleep(0.1)   #休眠0.1s
    n = temp-1        #数量-1
    print("购买成功，剩余%d张电影票"%n)
    mutex.release()    #释放锁

if __name__ == '__main__':
    mutex = Lock()  #实例化Lock类
    t_l = []
    for i in range(10):
        t = Thread(target=task)
        t_l.append(t)
        t.start()
    for t in t_l:
        t.join()
