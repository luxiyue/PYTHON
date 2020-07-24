'''
假设大家大家根据自己的实际情况，统计出来你和同桌的各自从11岁到30岁
每年交往的女（男）朋友的数量，请在一个图中绘制出该数据的折线图，以便于
比较自己和同桌20年间的差异，同时分析每年交男女朋友的数量走势
'''
from matplotlib import pyplot as plt
from matplotlib  import font_manager

my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/MSYH.ttc")

y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]

x = range(11,31)

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)

#linestyle设置线的格式
#linestyle设置线的颜色
plt.plot(x,y_1,label="自己",color="orange",linestyle=':')
plt.plot(x,y_2,label="同桌",color="cyan",linestyle='-.')

#设置x轴刻度
_xtick_labels =["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels,fontproperties=my_font)
# plt.yticks(range(0,9))

#绘制网格
plt.grid(alpha=0.3,linestyle=":")#里面的第一个参数设置透明度

#添加图例（要求plot函数里面设置label参数）,就是告诉你每根线的意义
plt.legend(prop=my_font,loc="upper left")#注意只有这里设置字体的参数不一样(prop)

#展示
plt.show()