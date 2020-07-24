import numpy as np

us_file_path = "US_video_data_numbers.csv"

t1 = np.loadtxt(us_file_path,delimiter=",")#delimiter确定分割符
#unpack的功能是转置功能
t2 = np.loadtxt(us_file_path,delimiter=",",unpack=True)

print(t1)
print("*"*100)
print(t2)

print("*"*100+"12312")
#取行
# print(t2[2,:])#取第三行  后面的,:可以删掉  ，下面的数据都可以  把,:加上去
# print()
# print(t2[1:])#取第2行及其以后的行数
# print()
# print(t2[[0,2]])#取第一行和第三行，注意内部还有中括号

#取列
# print(t2[:,0])
# #取连续的多列
# print(t2[:,2:])
# #取不连续的多列 第1列 和 第三列
# print(t2[:,[0,2]])

#取多行和多列,取第三行 第四列的值
# print(t2[2,3])#类型是numpy.int64
# #取多行和多列，取第三行到第五行，第二列到第四列的结果
# b = t1[2:5,1:4]
# print(b)


#取多个不相邻的点(0,0)和(2,1)两个点
print(t1[[0,2],[0,1]])










print("*"*100)







#这里补充一下转置的方法：
t = np.arange(24).reshape((4,6))
print(t)
#转置方法1
print(t.transpose())
#转置方法2
print(t.T)
#转置方法3
print(t.swapaxes(1,0))