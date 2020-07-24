#这个和前面的不一样的是，这篇代码画的是
# 散点图
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/MSYH.ttc")

y_3 = [11,17,16,11,12,11,12,6,6,7,8,12,15]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22]

x_3 = range(1,14)
x_10 = range(21,34)


plt.figure(figsize=(20,8),dpi=80)

plt.scatter(x_3,y_3,label="3月份")
plt.scatter(x_10,y_10,label="10月份")

#调整x轴的刻度
_x = list(x_3)+list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels+= ["10月{}日".format(i-20) for i in x_10]
plt.xticks(_x,_xtick_labels,fontproperties=my_font,rotation=45)


#添加图例
plt.legend(loc="upper left",prop=my_font)

#添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度",fontproperties=my_font)
plt.title("温度时间表",fontproperties=my_font)

#展示
plt.show()