#-*-coding:utf-8-*-
from multiprocessing import Process

def plus():
    print("----子进程1开始------")
    global g_num
    g_num += 50
    print('g_num is %d'% g_num)
    print('----子进程1结束------')

def minus():
    print("----子进程2开始------")
    global g_num
    g_num -= 50
    print('g_num is %d' % g_num)
    print('----子进程1结束------')

g_num = 100 #定义一个全局变量

if __name__ == '__main__':
    print("---------主程序开始-------")
    print("g_num is %d"%g_num)
    p1 = Process(target=plus)
    p2 = Process(target=minus)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("-------主进程结束-----")

#从运行结果可以看出,g_num在父进程和两个子进程中的初始值都是100，也就是全局变量g_num在
#一个进程中的结果，没有传到下一个进程中，及进程之间没有共享信息