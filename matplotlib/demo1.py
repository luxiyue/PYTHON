from matplotlib import pyplot as plt

a=range(0,10)
b=[5,6,7,1,6,4,9,5,1,2.5]

#设置图片大小
plt.figure(figsize=(20,8),dpi=80)

#绘图
plt.plot(a,b)

#设置x,y轴的刻度
# plt.xticks(a)
_w = ["hello,{}".format(i) for i in range(0,10)]
plt.xticks(a,_w)
plt.yticks(range(0,10))

#保存图片
# plt.savefig('./p.png')

#展示图片
plt.show()