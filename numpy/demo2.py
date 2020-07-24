import numpy as np

t1 = np.arange(12)
print(t1)
print(t1.shape)

print("=================================")

t2 = np.array([[1,2,3],[4,5,6]])
print(t2)
print(t2.shape)

print("=================================")

t3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t3)
print(t3.shape)

print("=================================")
#改变维度
t4 = np.arange(12)
print(t4)
print(t4.reshape(3,4))

print("=================================")

t5 = np.arange(24).reshape((2,3,4))
print(t5)
#正确的转为1维数组的方法
print(t5.reshape(24,))
#下面两个都是错误的转化方法
print(t5.reshape(24,1))
print(t5.reshape(1,24))

print("=================================")
t6 = t5.reshape((t5.shape[0]*t5.shape[1]*t5.shape[2],))
print(t6)


print("=================================")
t7=t5.reshape(4,6)
print(t7)
print(t7+3)#t7每个元素加3
print(t7/2)#t7每个元素/2
#nan意思是not a number      inf代表的意思是无穷大  infinity
print(t7/0)

print("=================================")
#这就是矩阵的加减
t8 = np.arange(100,124).reshape((4,6))
print(t7+t8)

print("=================================")
#t7的每行都减去t9
t9 = [0,1,2,3,4,5]
print(t7-t9)

print("==============10=================")
t10 = np.arange(4).reshape((4,1))
print(t10)
print(t7)
#t7每列 都减去了t10
print(t7-t10)


#!!!!!!!!!!!!!!!!!!如果一维数组的长度  没有  和另外数组对应的行数和列数相等    则相加减会报错