#时间序列
import pandas as pd
import numpy as np
# print(pd.date_range(start="20171230",end="20180131",freq="D") )#D表示每个一天
# print(pd.date_range(start="2017-12-30",end="20180131",freq="D") )
# print(pd.date_range(start="2017/12/30",end="20180131",freq="D") )
# print(pd.date_range(start="2017*12*30",end="20180131",freq="D") )#用*号隔开是不行的
# print(pd.date_range(start="20171230",end="20180131",freq="10D") )
# print(pd.date_range(start="20171230",periods=10,freq="10D"))#periods指定
# print(pd.date_range(start="20171230",periods=10,freq="M"))#M代表月份
# print(pd.date_range(start="20171230",periods=10,freq="MS"))#Ms每月第一个日历日
# print(pd.date_range(start="20171230",periods=10,freq="H"))#H每小时
print(pd.date_range(start="2017-12-30 10:10:30",periods=10,freq="H"))


# index=pd.date_range("20170101",periods=10)
# df = pd.DataFrame(np.random.rand(10),index=index)
# print(df)
