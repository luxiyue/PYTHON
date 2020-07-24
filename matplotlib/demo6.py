from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:/WINDOWS/Fonts/MSYH.ttc")

a=["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_14=[15746,312,4497,319]
b_15=[12357,156,2045,168]
b_16=[2358,399,2358,362]

b_width =0.2

x_14 = list(range(len(a)))
x_15 = [i+b_width for i in x_14]
x_16 = [i+b_width*2 for i in x_14]

plt.figure(figsize=(20,8),dpi=80)

plt.bar(x_14,b_14,width=b_width,label="9月14日")
plt.bar(x_15,b_15,width=b_width,label="9月15日")
plt.bar(x_16,b_16,width=b_width,label="9月16日")


#设置图例
plt.legend(prop=my_font)



plt.xticks(x_15,a,fontproperties=my_font)

plt.show()