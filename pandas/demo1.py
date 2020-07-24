#pandas主要就是处理字典类型的数据
import string
import pandas as pd

a = pd.Series([1,2,31,12,3,4])#Series：一维，带标签数组，如果不指定index,则用的是默认的索引
print(a)
print(type(a))
print(a[a>10])#打印值大于10的字典

b = pd.Series([1,23,2,2,1],index=list("abcde"))
print(b)

temp_dict = {"name":"xiaohong","age":30,"tel":10086}
c = pd.Series(temp_dict)
print(c)
print(list(c.index)[:2])
print(list(c.values)[:2])

print("c的age值：",c["age"])
print("c的tel",c[-1])
print(c[["age","tel"]])

print("*"*100)################################################
dic = {string.ascii_uppercase[i]:i for i in range(10)}
d = pd.Series( dic )
print(d)
e = pd.Series( dic,index=list(string.ascii_uppercase[5:15]) )
print(e)
