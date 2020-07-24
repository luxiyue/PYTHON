import numpy as np

a = np.arange(24).reshape(4,6).astype(float)
b = a.copy()
a[:,0]=0
#如果axis=0算的是每列的结果，=1算的是每行的结果。不写就算计算所有数据的结果
print("如果a中没有值=nan则总和为：",np.sum(a,axis=0))
a[3,3]=np.nan
a[2,4]=np.nan
print("如果a中有值=nan则总和为：",np.sum(a))
print(a)
print(np.count_nonzero(a))#输出不为零的个数
print(np.count_nonzero(a!=a))#输出nan的个数

print("*"*100)
print(a!=a)
print(np.isnan(a))
#可以发现上面输出的结果是一样的，所以
print(np.count_nonzero(np.isnan(a)))#输出nan的个数

#计算每列的均值
print("每列的均值",a.mean(axis = 0))
#计算每列的中值
print("每列的中值",np.median(a,axis=0))
#计算每行的最大值
print("每行的最大值",a.max(axis=1))
#计算每行的最小值
print("每行的最小值",a.min(axis=1))
#计算每行的极值
print("每行的极值",np.ptp(a,axis=1))
#计算标准差
print("b的标准差",b.std(axis=None))