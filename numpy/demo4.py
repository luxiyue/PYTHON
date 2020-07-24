import numpy as np
#numpy的赋值操作

t = np.arange(24).reshape(4,6)
print(t)
print(t<10)
t[t<10] = 3#另值小于10的部分=3
print(t)

print("="*100)
#np的三元运算符

t2 = np.where(t<=3,100,300)#小于3的部分设成100  大于3的部分设为300
print(t2)

t3 = t.clip(10,18)#将小于10的替换为10，大于18的替换成18
print(t3)
t3 = t3.astype(float)
t3[3,3]=np.nan
print(t3)


print("="*100)
g = np.mat('4 3; 2 1')
print(g)