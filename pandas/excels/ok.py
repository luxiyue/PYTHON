import pandas as pd

df = pd.read_csv("a.xlsx")#他会默认将第一行设置为列名
print(df)
# print(df)
# print("=========")
ys = {"1":"星期一","2":"星期二","3":"星期三","4":"星期四","5":"星期五","6":"星期六","7":"星期日"}
dic = {}
for i in range(1,8):
    # print(df[ys[str(i)]])
    for j in df[ys[str(i)]]:
        if str(j) not in dic:
            dic[str(j)] = 1
        else:
            dic[str(j)] += 1
print(dic)

