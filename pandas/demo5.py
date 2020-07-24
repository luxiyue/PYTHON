#pandas对缺损数据的处理 nan
import numpy as np
import pandas as pd
w = pd.DataFrame(np.arange(24).reshape(4,6),index=list("abcd"),columns=list("XCVBNM") )
w.iloc[2:,:2] = np.nan
print(w)
# print(pd.isnull(w))#nan的地方为True 其余的地方全是False
# print(pd.notnull(w))#nan的地方为False 其余的地方为True
#
# print(w[pd.notnull(w["X"])])#选择中w中 X列不为Nan的行

#删除有nan的行
# w = w.dropna(axis=0)
# print(w)
#删除有nan的列
# w = w.dropna(axis=1)
# print(w)

# print(w.dropna(axis=0,how="all"))#删除全部为nan的一行
# #how的默认值为any ，删除默认有nan的行
# print(w.dropna(axis=0,how="any",inplace=True))  #这里的inplace参数的意义等价于 w=w.dropna(axis=0,how="any")
#
# print(w)




#填充nan
print(w.fillna(0))#将nan的部分填充为0，但是没有意义
print("下面的函数是计算每列的平均值：")
print(w.mean())
print("将平均值填充到等于Nan的地方")
print(w.fillna(w.mean()))

print()
#只填充X列的Nan
w["X"] = w["X"].fillna(w["X"].mean())
print(w)
w["X"][1]=np.nan#这里会报警告   但是可以忽略
print(w["X"].mean())  #答案是2  因为：( 3+3)/3 = 2



#有些数据缺损 的值是0   处理方法就是将该0先变成nan





