from multiprocessing import Process

#执行子进程代码
def test(interval):
    print("我是子进程")

#执行主程序
def main():
    print("主进程开始")
    p = Process(target=test,args=(1,)) #实例化Process进程类
    p.start() #启动子进程
    print("主进程结束")

if __name__ == '__main__':
    main()

