#直方图
from matplotlib import pyplot as plt
from matplotlib import font_manager

a=[131,98,125,131,124,139,131,117,128,108,135,138,131,102,107,114,119,128,121,141,95,106,131,138,125,127,110,104,106]

#计算组数
d = 3 #组距
num_bins = (max(a)-min(a))//d

# plt.figure(figsize=(20,8),dpi=80)

#一般来说能够使用plt.hist方法的是那些没有统计过的数据
plt.hist(a,num_bins,normed=True)#如果加上后面的东西，显示的就是占比

plt.xticks(range(min(a),max(a)+d,d))

plt.grid()

plt.show()