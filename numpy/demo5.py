#数组的拼接

import numpy as np

t1 = np.arange(0,12).reshape(2,6)
t2 = np.arange(12,24).reshape(2,6)
print(t1)
print(t2)
t3 = np.vstack((t1,t2))#垂直拼接
print(t3)
t4 = np.hstack((t1,t2))#水平拼接
print(t4)

#交换数据的行列
print("===="*30)
print(t3)
t3[[1,2],:] = t3[[2,1],:]#交换第二行和第三行
print(t3)
t3[:,[0,2]] = t3[:,[2,0]]#交换第1列和第3列
print(t3)
