import pandas as pd
from pymongo import MongoClient
import numpy as np

df = pd.read_csv("A.csv")#他会默认将第一行设置为列名
#他还可以读取数据库sql语句
print(df)
print()
df = df.sort_values(by="Count_AnimalName",ascending=True)#如果ascending=False,则为降序
print(df)

print()
print(df[:3])#通过切片的方式取前3行

print()
print(df["Row_labels"])#只取Row_labels列的数据  数据类型为Series
print("="*100)
#下面的代码运行不出来，没有意义
# client = MongoClient()
# collection = client["douban"]["tv1"]
# data = list(collection.find())
# print(data)
# t1 = data[0]
# t1 = pd.Series(t1)
# print(t1)

#下面的index指定行索引  columns指定列索引   如果不要这两个属性则默认是自然数作为索引
q = pd.DataFrame(np.arange(12).reshape(3,4),index=list("abc"),columns=list("wxyz"))
print( q )

print()

dic = {"name":["xiaoming","xiaogang"],"age":[20,32],"tel":[10086,10010]}
p = pd.DataFrame(dic)
print(type(p))
print(p)

print()
dic2 = [{"name":"xiaohong","age":"32","tel":10010},{"name":"xiaogang","tel":10000},{"name":"xiaowang","age":22}]
o = pd.DataFrame(dic2)
print(o)
print("行索引",o.index)
print("列索引",o.columns)
print("o.shape:",o.shape)
print(o.dtypes)
print("数据的维度：",o.ndim)
#显示头几行  不写参数默认是5行吧....
print(o.head(1))#输出前一行
#显示后几行
print(o.tail(1))#输出最后一行


#o的概括
print("="*90)
print(o.info())
print()
print(o.describe())