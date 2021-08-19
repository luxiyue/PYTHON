import random

import numpy as np

t1 = np.array([1,2,3,])
print(t1)
print(type(t1))#<class 'numpy.ndarray'>

t2 = np.array(range(10))
print(t2)
print(type(t2))


#运行发现，下面的代码的效果和上面的效果一样
t3 = np.arange(4,10,2)
print(t3)
print(type(t3))
print(t3.dtype)

t4 = np.array(range(1,4),dtype="float32")#float i1
print(t4)
print(t4.dtype)#dtype 是输出每个元素的类型

#numpy中的bool类型，不为零就是true
t5 = np.array([2,1,0,1,0,0],dtype=bool)
print(t5)
print(t5.dtype)

#调整数据类型
t6 = t5.astype("int8")
print(t6)
print(t6.dtype)

#numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

#取两位
t8  = np.round(t7,2)
print(t8)
print(t8.dtype)

print("----------------------")
p = [[1,2,3],[4,5,6],[7,8,9]]
p1 = np.array(p)
print(p1)

