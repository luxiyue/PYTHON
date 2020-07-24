import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/MSYH.ttc")
file_path = "starbucks_store_worldwide.csv"
df = pd.read_csv(file_path)
'''
使用matplotlib 呈现出店铺总数排名前10的国家
'''
#准备数据
# data1 = df.groupby(by="Country").count()["Brand"].sort_values(ascending=False)[:10] #默认为升序  ascending=False表示降序
# _x = data1.index
# _y = data1.values
# #画图
# plt.figure(figsize=(20,8),dpi=80)
# plt.bar(range(len(_x)),_y)
# plt.xticks(range(len(_x)),_x)
# plt.show()

'''
使用matplotlib 呈现出每个中国每个城市的店铺数量
'''
df = df[df["Country"]=="CN"]
data1 = df.groupby(by="City").count()["Brand"].sort_values(ascending=False)[:50] #默认为升序  ascending=False表示降序
_x = data1.index
_y = data1.values
#画图
plt.figure(figsize=(20,8),dpi=80)
plt.bar(range(len(_x)),_y,width=0.3,color="orange")
plt.xticks(range(len(_x)),_x,font_properties=my_font,rotation=45)
plt.show()