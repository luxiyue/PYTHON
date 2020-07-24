import numpy as np

t = np.arange(24).reshape(4,6)
#创建一个全为0的数组
a1 = np.zeros((t.shape[0],1)).astype(int)
#创建一个权威1的数组
a2 = np.ones((t.shape[0],1)).astype(int)

t1 = np.hstack((t,a1))
t2 = np.hstack((t,a2))

#拼接两组数据
final_data = np.vstack((t1,t2))
print(final_data)



print(np.zeros((3,4)))
w = np.eye(3)
print(w)#创建一个3行3列的单位矩阵  （对角线为1 其余部分为0的行列式）
print(np.argmax(w,axis=0))#求出每一行最大数的索引
w[w==1]=-1
#axis区分行和列  这是我的猜想   需要我以后自己验证
print(np.argmin(w,axis=1))#求出每一列最小数的索引
#如果 想以后每次得到的结果相同 就加上这个
np.random.seed(10)
b=np.random.randint(10,20,(4,5))
print(b)#产生4行5列  值在10~20之间的整数
