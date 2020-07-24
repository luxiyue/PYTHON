import pandas as pd
import numpy as np
t = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("WXYZ"))
print(t)
print()

#通过标签索引 获取行列数据
print(t.loc["a","Z"])#类型为numpy.int64
print()
print(t.loc["a",:])#类型为Series
print()
print(t.loc[:,"Y"])
print()
print(t.loc[["a","c"],:])#取两行  类型为DataFrame
print()
print(t.loc["a":"c",["W","Z"]])#取W,Z两列的   a~c行

# print()
# #通过位置获取行数据
# print(t.iloc[1,:])
# print()
# print(t.iloc[:,2])
# print()
# print(t.iloc[:,[2,1]])
# print()
# print(t.iloc[[0,2],[2,1]])#取的是（0,2）（0,1）（2,2）（2,1）这几个点
# print()
# print(t.iloc[1:,:2])#取第2行后面的每一行（包括第二行） 和  第第三列前面的每一列（不包含第第三列）的交集

# print()
# t.iloc[1:,:2]=np.nan#注意必须得加上 iloc
# print(t)

