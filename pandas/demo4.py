import pandas as pd
import numpy as np

#pandas读取csv中的文件
df = pd.read_csv("A.csv")
print(  df[ df["Count_AnimalName"] < 10000 ]   )
print()
#且用&  或用|    不同的条件之间需要用括号括起来
print( df[ (df["Count_AnimalName"] < 10000 ) & (5000 <  df["Count_AnimalName"]) ])
print()
p = pd.DataFrame([["dasda","dadadwed","qreqr"],["dad","dthft","yuiy"]],index=list("ab"),columns=list("WXY"))
print(p)
print("++++++++++")
print(p["Y"].str.len()>4)
print("++++++++++")
print(p["Y"].str.contains("y"))

