#对星巴克店铺的统计数据进行分析
import pandas as pd
import numpy as np
file_path = "starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())
#根究国家进行分组   grouped对象 1.可以进行遍历 2.可以调用聚合方法
grouped = df.groupby(by = "Country")
# print(grouped)
# 1.可以进行遍历
# for i,j in grouped:
#     print(i)
#     print("-"*100)
#     print(j,type(j))
#     print("*"*100)
# 2.可以调用聚合方法
# print(grouped.count())


#统计中国和美国星巴克的数量：
# country_count = grouped["Brand"].count()
# # print(country_count)
# print("美国星巴克的数量",country_count["US"])
# print("中国星巴克的数量",country_count["CN"])



#统计中国每个省店铺的数量
# china_data = df[df["Country"] == "CN"]
# #自我理解：我认为加上count的意义在于 呈现分组之后的 “所有” 数据
# grouped = china_data.groupby(by="State/Province").count()["Brand"]
# print(grouped)


#数据按照多个条件进行分组,返回Series
# grouped = df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
# print(grouped)
# print(type(grouped))


#数据按照多个条件进行分组,返回Dataframe
grouped1 = df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count()
# grouped2 = df.groupby(by=[df["Country"],df["State/Province"]])[["Brand"]].count()
# grouped3 = df.groupby(by=[df["Country"],df["State/Province"]]).count()[["Brand"]]
# print(grouped2)
# print(type(grouped2))

##################################################################################################











#索引的方法和属性
print(grouped1.index)
t1 = pd.DataFrame(np.arange(8).reshape((2,4)),index=list("AB"),columns=list("abcd"))
#对索引修改
t1.index = ["a","b"]

print(t1)
print(t1.reindex(["a","f"]))
print("将a作为索引")
print(t1.set_index("a",drop=False))
print("将a作为索引，并且drop=True是默认值  删去a这一列")
print(t1.set_index("a",drop=True))

#unique
print(t1["a"].unique())
print(t1.set_index("b").index.unique())
print(t1.set_index("b").index)
print(t1.set_index(["a","b"]).index)


a = pd.DataFrame({'a':range(7),"b":range(7,0,-1),'c':['one','one','one','two','two','two','two'],'d':list("hjklmno")})
# print(a)
b = a.set_index(['c','d'])
print(b)
# #注意必须是下面这个顺序  先指定列  在指定第一个行索引 再指定第二个行索引
print("取第二行最后那一列的值：",b["b"]["one"]["j"])
#或者用loc来操作
#取第一行的数据
print(b.loc["one"].loc["h"])
print("取第一行最后一列的数据：",b.loc["one"].loc["h"]["b"])
print(b.swaplevel())
print(b.swaplevel().loc["h"])
# print()
# d = a.set_index(['d','c'])["a"]
# print(d)
# print()
# # print(d["j"]["one"])
# #将行索引交换一下顺序（ 自我感觉下面的语句和 b["a"]的效果一样 ）
# print(d.swaplevel())
# print()
# print(d.swaplevel()["one"])
