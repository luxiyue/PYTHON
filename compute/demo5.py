class Drink:
    brand = ""  #定义变量，饮品的厂商
    price = 0   #定义变量，饮品的价格
    def __init__(self,brand,price):#构造方法
        self.brand = brand;
        self.price = price;
    def message(self): #定义一个抽象函数，用于显示产品信息
        pass

class Milk(Drink):  # milk类 继承了 Drink 类
    def __init__(self,brand,price):#构造方法
        super(Milk,self).__init__(brand,price) #执行父类的构造方法
    def message(self):#重写（实现）了Drink的message方法
        print(self.brand ," 牛奶真的是 好喝的不得了~  只需要",self.price,"元")

class Beer(Drink): #beer 类继承了 Drink类
    def __init__(self,brand,price):#构造方法
        super(Beer,self).__init__(brand,price) #执行父类的构造方法
    def message(self):#重写（实现）了Drink的message方法
        print(self.brand ," 啤酒喝的 非常的过瘾~ 只需要",self.price,"元")

if __name__ == '__main__': #主函数，相当于java的main函数
    milk = Milk("伊利",4)
    beer = Beer("雪花",6)
    milk.message()
    beer.message()



