#拼接问题
import pandas as pd
import numpy as np

#注意index 如果改成EF  则后面运行的都是NAN  说明join完全是按照行索引进行合并的
t2 = pd.DataFrame(np.zeros((2,5)),index=list("AB"),columns=list("VWXYZ"))
print("t2为：")
print(t2)
t1 = pd.DataFrame(np.ones((3,4)),index=list("ABC"))
print("t1为：")
print(t1)


#按照行索引进行合并#说白了就是sql中的   left join
print("以t1为准！！")
print(t1.join(t2))
print("以t2为准！！")
print(t2.join(t1))

print("&*"*100)

t3 = pd.DataFrame(np.ones((2,4)),index=list("AB"),columns=list("abcd"))
t3.loc["A","a"] = 100
print(t3)
t4 = pd.DataFrame(np.zeros((3,3)),columns=list("fax"))
t4.loc[1,"a"] = 1
print(t4)
print(t3.merge(t4,on="a"))

t4 = pd.DataFrame(np.arange(9).reshape((3,3)),columns=list("fax"))
# t4.loc[1,"a"] = 1
print(t4)
#how的默认值就是inner笛卡尔积.,相当与数据库的内连接 outer left right
#下面的on 还可以拆成 left_on right_on  用与关联两片数据的字段
print(t3.merge(t4,on="a",how="right"))