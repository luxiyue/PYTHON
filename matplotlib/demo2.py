from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager
import random

#下面的这块，我试了一下，没有用
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.rc('font',**font)
# matplotlib.rc('font',family='MicroSoft YaHei',weight='blod')



#fname指定的是字体文件的位置
my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/MSYH.ttc")

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
#设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

#绘图
plt.plot(x, y)

# 调整x的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
# 取步长，数字和字符串一一对应，数据的长度一样
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45,fontproperties=my_font)  # rotation参数用来控制旋转的度数，fontproperties控制字体


#添加描述信息
plt.xlabel("时间",fontproperties=my_font)
plt.ylabel("温度 单位（‘C）",fontproperties=my_font)
plt.title("10点到12点每分钟的气温变化情况",fontproperties=my_font)


plt.show()
