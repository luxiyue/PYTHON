import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/MSYH.ttc")

file_path = "books.csv"
df = pd.read_csv(file_path)
# print(df.head(1))
# print(df.info())
'''
求不同年份书的数量
'''
# data1 = df[pd.notnull(df["original_publication_year"])] #选出original_publication_year该列  不为nan的数据
# grouped = data1.groupby(by="original_publication_year").count()["books_count"]
# print(grouped)
# _x = grouped.index
# _y = grouped.values
# plt.figure(figsize=(20,8),dpi=80)
# plt.bar(range(len(_x)),_y,color="orange")
# plt.xticks(list(range(len(_x)))[::10],_x[::10],font_properties=my_font,rotation=45)
# plt.show()
'''
不同年份书的平均评分情况
'''
data1 = df[pd.notnull(df["original_publication_year"])]
grouped = data1["average_rating"].groupby(by=data1["original_publication_year"]).mean()
print(grouped)
_x = grouped.index
_y = grouped.values
plt.figure(figsize=(20,8),dpi=80)
plt.plot(range(len(_x)),_y)
plt.xticks(list(range(len(_x)))[::10],_x[::10].astype(int),rotation=45)
plt.show()